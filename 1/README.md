# Part 1

__[slide 4]__

Check the list of docker images:
```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

Get our first docker image (__syntax__ `docker pull IMAGE`):
```bash
$ docker pull python:alpine
```

Check the list of docker images:
```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
python              alpine              8eb1c554687d        3 weeks ago         90.4MB
```

__[slide 5]__

Run the our first container:
```bash
$ docker run python:alpine
```

Nothing happened, since there's no pre-configured command to run.

Let's indicate a command then (__syntax__ `docker run IMAGE CMD`):
```bash
$ docker run python:alpine python --version
Python 3.6.5
```

### Hello world!

Python:
```bash
$ python -c 'print("hello world!")'
hello world!
```

Python in Docker:
```bash
$ docker run python:alpine python -c 'print("hello world!")'
hello world!
```

Alternative:
```bash
$ echo "hello world!"
hello world!
$ docker run python:alpine echo "hello world!"
hello world!
```

### Listing containers running

Let's check the list of containers running:
```bash
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

Well, nothing as expected.

Let's run a container for some time then.

```bash
$ man sleep
$ docker run python:alpine sleep 10
```

In the next 10 seconds, run in another terminal:
```bash
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED                  STATUS              PORTS               NAMES
6e6be0c8f31c        python:alpine       "sleep 10"          Less than a second ago   Up 1 second                             eloquent_lichterman
```

__[slide 5]__

### Let's create simple container

Our first `Dockerfile`:

```bash
FROM python:alpine

CMD python -c 'print("hello world!")'
```

Let's now build the docker image with a repository and tag,
as in `python:alpine`
(__syntax__ `docker build -f FILE -t IMAGE DIR`):
```bash
$ docker build -f Dockerfile -t vitorenesduarte/tutorial:hello .
```

And check that the new image is in the list of images:
```bash
$ docker images
REPOSITORY                 TAG                 IMAGE ID            CREATED              SIZE
vitorenesduarte/tutorial   hello               49aa76850e83        About a minute ago   90.4MB
python                     alpine              8eb1c554687d        3 weeks ago          90.4MB
```

Let's run our app:
```bash
$ docker run vitorenesduarte/tutorial:hello
hello world!
```

But this is not how we write apps, right?

Let's then create a file named `app.py` with:
```python
print("hello world!")
```

Verify it is okay:
```bash
$ python app.py
hello world!
```

And modify `Dockerfile` to:

```bash
FROM python:alpine

COPY app.py /

CMD python app.py
```

Let's build the image again:
```bash
$ docker build -t vitorenesduarte/tutorial:hello .
```

Notice we didn't indicate which file to use.
Docker tries to find a file named `Dockerfile` in
the directory passed as argument.

Verify `app.py` was indeed copied to the docker image:

```bash
$ docker run vitorenesduarte/tutorial:hello ls | grep app
app.py
```

Let's run it again:
```bash
docker run vitorenesduarte/tutorial:hello
hello world!
```

__[slide 7]__

__[slide 8]__

Create file `docker-compose.yml` with:
```yml
version: "3"
services:
  app:
    build: .
```

Now build and run with:

```bash
$ docker-compose up --build
```

Change `docker-compose.yml` to:

```yml
version: "3"
services:
  app:
    build: .
  sleeper:
    build: .
    command: sleep 10
```

And again, in another terminal:
```bash
$ docker ps
```
