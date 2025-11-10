from fastapi import FastAPI
from routers import orders

app = FastAPI()

app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Welcome to Restaurant API"}
