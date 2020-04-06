from fastapi.testclient import TestClient

from main import app

import pytest 

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}

# @pytest.mark.parametrize('method', ['get', 'post', 'put', 'delete'])
def test_method():
    response = client.get('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}


# @pytest.mark.parametrize("name", ['Zenek', 'Marek', 'Alojzy Niezdąży'])
# def test_hello_name(name):
#     response = client.get(f'/hello/{name}')
#     assert response.status_code == 200
#     assert response.json() == {'message': f'Hello {name}'}