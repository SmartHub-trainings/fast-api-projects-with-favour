from fastapi import APIRouter
from schema.products import CreateProduct

products_router = APIRouter()

products = []
@products_router.get("/products",tags=["Products"])
def get_all_products():
    return {
        "message":"All products",
        "statusCode":200,
        "data":products
    }
    
@products_router.get("/products/{product_id}",tags=["Products"])
def get_product_by_id(product_id:int):
    return {
        "message":"Product by id",
        "statusCode":200,
        "data":products[product_id]
    }

@products_router.post("/products",tags=["Products"])
def create_product(product:CreateProduct):
    products.append(product)
    return {
        "message":"Product created",
        "statusCode":201,
        "data":product
    }
    
    
    