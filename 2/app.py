from flask import Flask
app = Flask(__name__)

import sys
id = sys.argv[1] if len(sys.argv) > 1 else "ups!"

@app.route("/")
def hello():
    return "Hello World! (from " + id + ")"

app.run(host="0.0.0.0", debug=True)
