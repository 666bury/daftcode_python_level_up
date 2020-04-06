from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World during the coronavirus pandemic!"}

class HelloNameResp(BaseModel):
    message: str

# @app.get('/hello/{name}', response_model=HelloNameResp)
# def hello_name(name: str):
#     return HelloNameResp(message=f'Hello {name}')

@app.get('/method')
def method():
    return {"method": "GET"}


@app.post('/method')
def method():
    return {"method": "POST"}


@app.put('/method')
def method():
    return {"method": "PUT"}


@app.delete('/method')
def method():
    return {"method": "DELETE"}