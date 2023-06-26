from fastapi import FastAPI
from typing import Dict
from models.credentials import SignIn, SignUp

app = FastAPI(prefix='/auth')


@app.post('/sign-in')
async def sign_in(data: SignIn) -> Dict[str, str]:
    return {'Hello': 'World'}


@app.post('/sign-up')
async def sign_up(data: SignUp) -> Dict[str, str]:
    return {'Hello': 'World'}
