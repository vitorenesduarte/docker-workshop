import util

BASE_PORT = 8000

id, children = util.parse_args()

def forward(l):
    # forward message to children
    for child in children:
        client = util.SimpleClient(port=BASE_PORT + child, retry=True)
        client.send(l)

def send(l):
    print(str(id) + " received: " + str(l))
    l.append(id)
    forward(l)

# create server
server = util.SimpleServer(port=BASE_PORT + id, verbose=True)
server.register_function(send)
print(server.list_functions())

# if 0, start sending
if id == 0: forward([id])

# server wait
server.wait()
