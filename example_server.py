import util

def add(x, y):
    return x * y

server = util.SimpleServer(port=8000, verbose=True)
server.register_function(add)
server.wait()
