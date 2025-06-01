from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_read_root_deve_retornar_ola_mundo():
    """
    Este teste tem 3 etapas (AAA)
    - A: Arrange    - Arranjo
    - A: Act        - Executa a coisa (o SUT)
    - A: Assert     - Garanta que A é A
    """

    # Arrange
    client = TestClient(app)

    # Ac
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_read_html_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/html')
    assert response.text == '<h1>Olá mundo!</h1>'
    assert response.status_code == HTTPStatus.OK
