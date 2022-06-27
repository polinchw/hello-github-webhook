import sys
import logging
import os
from flask import Flask, request

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger('main')

werkzeug = logging.getLogger('werkzeug')
werkzeug.setLevel(os.environ.get('WERKZEUG_LOGLEVEL', 'ERROR').upper())

# Port 9090
app = Flask("pyProm")

@app.route('/', methods=["GET"])
def hi():
    """Returns 'ArgoCD is amazing'

    Returns:
        str: 'ArgoCD is amazing'
    """ 
    if request.method == "GET":
        return "ArgoCD is amazing.  Break it!", 200, None

    return "Bad Request", 400, None

@app.route('/health', methods=["GET"])
def health():
    """Returns 'OK'

    Returns:
        str: 'OK'
    """
    if request.method == "GET":
        return "OK", 200, None

    return "Bad Request", 400, None


@app.route('/demo', methods=["GET"])
def demo():
    if request.method == "GET":
        return "OK", 200, None

    return "Bad Request", 400, None


try:
    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=9090)
except RuntimeError:
    log.info('shutdown')