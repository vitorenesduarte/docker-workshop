# Part 2

__[slide 10]__

(you can copy the files from part 1 to another folder, and start from there)

Let's build a web app.

Go to [http://flask.pocoo.org/](Flask)!

```bash
$ pip install Flask
```

Change `app.py` to:
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run(host="0.0.0.0", debug=True)
```

Run the app and check [http://0.0.0.0:5000/](http://0.0.0.0:5000/):
```bash
$ python app.py
```

Remove the `sleeper` from `docker-compose.yml`:
```bash
version: "3"
services:
  app:
    build: .
```

Run `docker-compose up --build` and check [http://0.0.0.0:5000/](http://0.0.0.0:5000/).

It doesn't work. Why?

We need to expose and publish the container's port `5000` to the host (our machine):

```bash
version: "3"
services:
  app:
    build: .
    ports:
      - "3333:5000"
```

The above publishes container's port `5000` on host's port `3333`.

Run `docker-compose up` and [http://0.0.0.0:3333/](http://0.0.0.0:3333/).
