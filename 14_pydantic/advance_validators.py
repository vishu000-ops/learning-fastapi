from pydantic import BaseModel, Field, field_validator
from datetime import datetime
class Person(BaseModel):
    first_name : str
    last_name : str

    @field_validator('first_name', 'last_name')
    def name_must_be_capitalize(cls, V):
        if not V.istitle():
            raise ValueError('Names must be capitalized')
        return V


class User(BaseModel):
    email : str
    @field_validator('email')
    def normalize(cls, v):
        return v.lower().strip()

class Product(BaseModel):
    price : str

    @field_validator('price')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v