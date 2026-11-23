from fastapi import FastAPI
from database import create_table

from routes import books, users

app = FastAPI(
    title="Kitab Exchange API",
    description="A simple API for exchanging user books",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_table()

app.include_router(users.router)
app.include_router(books.router)


