import sys
import logging
from flask import Flask, request

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger('main')

# Port 8081
app = Flask("pyProm")


@app.route('/', methods=["GET"])
def hi():
    if request.method == "GET":
        return "OK", 200, None

    return "Bad Request", 400, None

try:
    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=9090)
except RuntimeError:
    log.info('shutdown')