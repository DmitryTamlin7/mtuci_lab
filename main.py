from  fastapi import FastAPI
import pyjokes
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def kalkulator(value1: int, value2: int, znak: str):
    if (znak == '+'):
        return value1 + value2

    if (znak == '-'):
        return value1 - value2

    if (znak == '*'):
        return value1 * value2

    if (znak == '/') and (value2 == 0):
        return 'АШИБКА'

    if (znak == '/'):
        return value1 / value2

    if (znak == '**'):
        return value1 ** value2

