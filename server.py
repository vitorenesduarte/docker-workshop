from util import SimpleServer

def add(x, y):
    return x * y

server = SimpleServer(port=8000, verbose=True)
server.register_function(add)
server.wait()
