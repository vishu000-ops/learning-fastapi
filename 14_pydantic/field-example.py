from pydantic import BaseModel
from typing import Dict, List, Optional

class Cart(BaseModel):
    user_id : int
    items : list[str]
    quantities : dict[str, int]

class Blog_post(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None

cart_data = {
    "user_id" : 123,
    "items" : ["laptop" , "mouse", "keyboard", "speaker"],
    "quantities" : {
        "laptop" : 1,
        "mouse" : 5,
        "keyboard" : 2,
        "speaker" : 10
    }
}

cart = Cart(**cart_data)
print(cart)