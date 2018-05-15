from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy

import signal, sys, time

import argparse

class SimpleServer:
    def __init__(self, host="localhost", port=8000, verbose=True):
        # create server listening on host:port
        self.verbose = verbose
        self.server = SimpleXMLRPCServer((host, port), logRequests=verbose)

        # register introspection functions:
        # - system.listMethods
        # - system.methodHelp
        # - system.methodSignature
        self.server.register_introspection_functions()

        # run server listener in background thread
        # - daemon: is main thread ends, this thread halts
        self.server_thread = Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

        # shutdown gracefully on SIGINT
        signal.signal(signal.SIGINT, self.__signal_handler__)

    def __signal_handler__(self, signal, frame):
        """
        Shutdown on SIGINT.
        (internal use)
        """
        if self.verbose:
            print("\n")
            print("CTRL+C was pressed... Shutting down!")

        self.server.shutdown()
        self.server_thread.join()
        sys.exit(0)

    def register_function(self, fun):
        """
        Register function passed as argument.
        """
        self.server.register_function(fun)

    def list_functions(self):
        """
        List functions registered, including introspection functions.
        """
        return self.server.system_listMethods()

    def wait(self):
        """
        Wait forever.
        """
        while True: time.sleep(10000)

class SimpleClient:
    def __init__(self, host="localhost", port=8000, retry=True):
        # create server url
        url = "http://" + host + ":" + str(port)

        # connect to server
        connected = False
        while not connected:
            try:
                self.client = ServerProxy(url)
                _ = self.list_functions()
                connected = True

            except Exception as e:
                print("Server " + url + " not connected yet.")

                if retry:
                    # try again in a second
                    print("Trying again in 1 second.")
                    time.sleep(1)
                else:
                    # if not retry, raise the exception
                    raise e

    def __getattr__(self, name):
        """
        Magic method dispatcher.
        """
        # see: https://github.com/python/cpython/blob/3.6/Lib/xmlrpc/client.py#L1468-L1470
        return self.client.__getattr__(name)

    def list_functions(self):
        """
        List functions registered in the server.
        """
        return [f for f in self.client.system.listMethods() if not f.startswith("system.")]

def parse_args():
    """
    Parse command-line arguments:
    Returns:
    - id
    - children ids
    Usage:
        PROG -i 0 -c 1
        PROG -i 1 -c 2
        PROG -i 2

    More info: https://docs.python.org/3.6/library/argparse.html
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="id", type=int)
    parser.add_argument("-c", dest="children", type=int, default=[], action="append")
    args = parser.parse_args()
    return args.id, args.children
