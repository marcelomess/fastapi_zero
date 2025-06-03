from http import HTTPStatus


def test_read_root_deve_retornar_ola_mundo(client):
    """
    Este teste tem 3 etapas (AAA)
    - A: Arrange    - Arranjo
    - A: Act        - Executa a coisa (o SUT)
    - A: Assert     - Garanta que A é A
    """

    # Arrange
    # client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_read_html_deve_retornar_ola_mundo(client):
    response = client.get('/html')
    assert response.text == '<h1>Olá mundo!</h1>'
    assert response.status_code == HTTPStatus.OK


def test_create_user_deve_criar_usuario(client):
    response = client.post(
        '/users/',
        json={
            'username': 'johndoe',
            'email': 'john@doe.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'john@doe.com',
        'username': 'johndoe',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'john@doe.com',
                'username': 'johndoe',
            }
        ]
    }


def test_get_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK


def test_get_user_by_id_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user_not_found(client):
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
