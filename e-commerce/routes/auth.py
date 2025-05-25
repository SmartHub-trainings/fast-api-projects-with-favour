from fastapi import APIRouter

auth_router = APIRouter()
users = []

@auth_router.post("/auth")
def register_user(user:dict):
    users.append(user)
    return {
        "message":"User registered",
        "statusCode":201,
        "data":user
    }
    
@auth_router.post("/auth/login")
def login_user(user:dict):
    user = users.find(lambda u: u["email"] == user["email"])
    if not user:
        return {
            "message":"User not found",
            "statusCode":404,
            "data":None
        }
    return {
        "message":"User logged in",
        "statusCode":200,
        "data":user
    }

