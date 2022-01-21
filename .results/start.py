from functools import reduce
import math
from sys import platform

import json
import subprocess
import re

from utils import get_argv_dict

argvs: dict = get_argv_dict()


with open('./config.json', 'r') as eyes:
    config: dict = json.load(eyes)

host = argvs.get('-h', '192.168.99.101')
ports = argvs.get('-p', '9001_8000_8008_9000')
requests = argvs.get('-r', config.get('limits', {}).get('requests', 2000))
connections = argvs.get('-c', config.get('limits', {}).get('connections', 100))
loading_tool = argvs.get('-t', 'loadtest')  # ab # all
strees_mode = argvs.get('-sm', 'doubling')
keep_alive = argvs.get('-k')

steps = config.get('steps')

strees_mode = 'm'

def main():    

    if strees_mode.startswith('l'):
        connection_range = range(steps.get('connections'), connections, steps.get('connections'))
        requests_range = range(steps.get('requests'), requests, steps.get('requests'))
    elif strees_mode.startswith('d'):
        # range_generate_for = lambda x, _limit: reduce(lambda i, acc: acc + [acc[-1] * 2], range(x, math.floor(_limit / x), [x]))
        def range_generate_for(x, _limit):
            range_list = reduce(lambda acc, i: acc + [acc[-1] * 2], range(math.floor(_limit / x)), [x])
            range_list = [i for i in range_list if i < _limit]
            if range_list and range_list[-1] < _limit:
                range_list.append(_limit)
            return range_list    

        connection_range = range_generate_for(steps.get('connections'), connections)
        requests_range = range_generate_for(steps.get('requests'), requests)
    elif strees_mode.startswith('m'):
        connection_range = [connections]
        requests_range = [requests]

    # connection_range = reduce(lambda acc, i: acc + [acc[-1] * 2], range(steps.get('connections'), math.floor(connections / steps.get('connections')), [steps.get('connections')]))
    # requests_range = reduce(lambda acc, i: acc + [acc[-1] * 2], range(steps.get('requests'), math.floor(requests / steps.get('requests')), [steps.get('requests')]))

    results = {}

    for _port in ports.split('_'):     

        results[_port] = {}

        for conn in connection_range:     

            results[_port][conn] = {}

            for reqs in requests_range:                

                load_test = f'{loading_tool} -c {conn} -n {reqs} {"-k " if keep_alive else ""}http://{host}:{_port}/'
                print(load_test)

                test = subprocess.Popen(load_test.split(' '), stdout=subprocess.PIPE, shell=True, )        # text=True, shell=True
                output, _ = test.communicate()    

                raw_result = output.decode(encoding='cp866' if platform.startswith('win') else 'utf-8')
                result = re.search(r'Requests per second:[\s]+(\d+)', raw_result)
                errors = re.search(r'Total errors:[\s]+(\d+)', raw_result)                

                if not result or not result.groups(): print('somethink went wrong...')
                else:
                    print(f'on {_port} port with a load of {conn} connections and {reqs} requests worth of Requests per second is: {result.groups()[0]}')                    

                if errors: print(f'errors: {errors.groups()[0]}')

                results[_port][conn][reqs] = result
    
    # save results to *.md as table

    # print(ls.stdout)    

if __name__ == '__main__':
    main()

