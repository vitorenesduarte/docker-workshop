from SimpleXMLRPCServer import SimpleXMLRPCServer, list_public_methods
from threading import Thread

import signal, sys, time
import xmlrpclib

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

    """
    Shutdown on SIGINT.
    (internal use)
    """
    def __signal_handler__(self, signal, frame):
        if self.verbose:
            print("\n")
            print("CTRL+C was pressed... Shutting down!")

        self.server.shutdown()
        self.server_thread.join()
        sys.exit(0)

    """
    Register function passed as argument.
    """
    def register_function(self, fun):
        self.server.register_function(fun)

    """
    List functions registered, including introspection functions.
    """
    def list_functions(self):
        return self.server.system_listMethods()

    """
    Wait forever.
    """
    def wait(self):
        while True: time.sleep(10000)

class SimpleClient:
    def __init__(self, host="localhost", port=8000):
        # create server url
        url = "http://" + host + ":" + str(port)

        # connect to server
        self.client = xmlrpclib.ServerProxy(url)

    """
    Magic method dispatcher.
    """
    def __getattr__(self, name):
        # see: https://github.com/python/cpython/blob/3.6/Lib/xmlrpc/client.py#L1468-L1470
        return self.client.__getattr__(name)

    """
    List functions registered in the server.
    """
    def list_functions(self):
        return [f for f in self.client.system.listMethods() if not f.startswith("system.")]
