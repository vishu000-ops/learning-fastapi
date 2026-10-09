from pydantic import BaseModel
class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True

product_one = Product(id=1, name=8, price=99.999, )
print(product_one)