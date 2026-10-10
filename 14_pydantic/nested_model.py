from pydantic import BaseModel,Field
from typing import Optional, List

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int
    name : str
    Address : Address