# docker-workshop

#### How to use [util.py](util.py)

- create file `example_server.py`:

```python
from util import SimpleServer

def add(x, y):
    return x * y

server = SimpleServer(port=8000, verbose=True)
server.register_function(add)
server.wait()
```

- create file `example_client.py`:

```python
from util import SimpleClient

client = SimpleClient(port=8000)
print("available functions: ")
print(client.list_functions())

print("2 + 3 = " + str(client.add(2, 3)))
print("5 + 2 = " + str(client.add(5, 2)))
```

- in one terminal, start the client:

```bash
$ python3 example_client.py
```

By default, the client retries to connect to the server every second.

- in another terminal, start the server:

```bash
$ python3 example_server.py
```

You can now gracefully stop this terminal with CTRL+C.
