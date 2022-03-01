import logging
import sys
import pytest
import os
os.environ['LOCATION_ID'] = 'TEST'
from main import app as flask_app

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger('main')


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(app, client):
    """
    Test the root context path /.
    Args:
        app: The flask app.
        client: The client.
    """
    res = client.get('/')
    assert res.status_code == 200
    expected ='ArgoCD is amazing'
    assert expected == res.get_data(as_text=True)


