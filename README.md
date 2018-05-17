# Docker/Kubernetes NECC Workshop - 23/05/2018

#### Prerequisites

- [Python 3](https://www.python.org/downloads/release/python-365/)


#### How to use [util.py](util.py)

- create file `example_server.py`:

```python
import util

def add(x, y):
    return x * y

server = util.SimpleServer(port=8000, verbose=True)
server.register_function(add)
server.wait()
```

- create file `example_client.py`:

```python
import util

client = util.SimpleClient(port=8000, retry=True)
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
