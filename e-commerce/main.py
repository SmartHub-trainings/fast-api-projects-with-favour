from fastapi import FastAPI
from routes.products import products_router 
from routes.auth import auth_router
from routes.default import router


app = FastAPI(
    title="E-commerce API",
    description="E-commerce API",
    version="1.0.0"
)

app.include_router(router,tags=["Default routes"])
app.include_router(products_router,tags=["Products"])
app.include_router(auth_router,tags=["Authentication routes"])



    
    
    
    
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app,port=8000)

