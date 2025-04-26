from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "World"}

@app.get('/greet')
async def greet_name(name:str) -> dict: 
    return {"message": f"Hellow {name}"}

@app.post('/login')
async def login(username: str, password: str, age: Optional[int] = 12)  -> dict:
    if username == 'savi':
        if password == "123":

            return {"message" : "login success"}
        
    return {"message" : "login failed"}