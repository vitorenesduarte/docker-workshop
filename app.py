import util

BASE_PORT = 8000

id, children = util.parse_args()

def send(msg):
    print(str(id) + " received: " + str(msg))

print(BASE_PORT + id)

# create server
server = SimpleServer(port=BASE_PORT + id, verbose=True)
server.register_function(send)

# create client
for child in children:
    client = SimpleClient(port=BASE_PORT + child, retry=True)
    client.send("hi")

# server wait
server.wait()
