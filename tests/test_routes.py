import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_status_route(client):
    response = client.get('/api/status')
    assert response.status_code == 200
    assert response.json == {"status": "API funcionando correctamente"}

