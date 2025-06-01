from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI Zero', version='0.1.1')


@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get(
    '/html',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
)
def read_html():
    return '<h1>Olá mundo!</h1>'
