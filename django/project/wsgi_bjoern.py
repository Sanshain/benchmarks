# from project.project.wsgi import application
from project.wsgi import application
import bjoern

host = '0.0.0.0'
port = 8000

# if __name__ == "__main__":
#     bjoern.listen(application, host, port, reuse_port=True)
#     bjoern.run()

bjoern.run(application, host, port, reuse_port=True)
