from pydantic import BaseModel, validator
from typing import Optional


class SignIn(BaseModel):
    username: str
    password: str


class SignUp(BaseModel):
    username: str
    password: str
    verify_password: str

    @validator('username')
    def username_already_taken(cls, username: str):
        if username == 'root': raise ValueError('username already taken')
        return username
    
    @validator('verify_password')
    def password_match(cls, verify_password, values , **kwargs):
        if 'password' in values and verify_password != values['password']: raise ValueError('passwords do not match')
        return verify_password
