from fastapi import APIRouter
from datetime import datetime


router = APIRouter()

@router.get("/")
def health_check():
    return {
        "message":"Welcome to our E-commerce API",
        "statusCode":200,
        "data":{
            "timestamp":datetime.now().isoformat(),
            "version":"1.0.0"
        }
    }
