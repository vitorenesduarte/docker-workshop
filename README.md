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

- in one terminal:

```bash
$ python example_server.py
```

- in another terminal:

```bash
$ python example_client.py
```

- you can now gracefully stop the first terminal with CTRL+C
