import sys
import timeit

default_times = 10000


def async_benchmark(fn):
    async def wrapper(*args, **kwargs):
        t = timeit.default_timer()
        r = await fn(*args, **kwargs)
        _delta = round(timeit.default_timer() - t, 4)
        print(fn.__name__ + ':', _delta, ' sec')
        if args:
            print(f"{round(args[0] / _delta, 2)} req/sec")
        else:
            print(f"{round(default_times / _delta, 2)} req/sec")
        return r

    return wrapper


def get_argv_dict() -> dict:
    argv_dict = {}
    for key in sys.argv:
        if key.startswith('-'):
            _index = sys.argv.index(key)
            if len(sys.argv) > _index + 1:  # and sys.argv[_index + 1].isdigit()
                argv = sys.argv[_index + 1]
                if not argv.startswith('-'):
                    argv_dict[key] = int(argv) if argv.isdigit() else argv
                    continue
            argv_dict[key] = True
    return argv_dict


def benchmark(fn):
    def wrapper(*args, **kwargs):
        t = timeit.default_timer()
        r = fn(*args, **kwargs)
        _delta = round(timeit.default_timer() - t, 4)
        print(fn.__name__ + ':', _delta, ' sec')
        if args:
            print(f"{round(args[0] / _delta, 2)} req/sec")
        else:
            print(f"{round(default_times / _delta, 2)} req/sec")
        return r

    return wrapper
