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
