from fastapi import FastAPI

app = FastAPI(
    title="Chai Menu API",
    description="An API for managing a menu of chai drinks.",
)

@app.get("/")
def welcome():
    return {"message": "Welcome to the Chai Menu API!"}