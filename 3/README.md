# Part 3

__[slide 12]__

(again, you can copy the files from one of the previous parts, and start from there)

(the following assumes `python3`)

#### How to use [util.py](util.py)

- create file `server.py`:

```python
import util

def add(x, y):
    return x * y

server = util.SimpleServer(port=8000, verbose=True)
server.register_function(add)
server.wait()
```

- create file `client.py`:

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
$ python client.py
```

By default, the client retries to connect to the server every second.

- in another terminal, start the server:

```bash
$ python server.py
```

You can now gracefully stop this terminal with CTRL+C.
