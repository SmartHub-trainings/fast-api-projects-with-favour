from pydantic import BaseModel
from typing import Optional


class BaseProduct(BaseModel):
    name: str
    price: float
    description: str
    stock: Optional[int] = 0
    
    
class CreateProduct(BaseProduct):
    pass