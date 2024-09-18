
from fastapi import FastAPI
import logging
import uuid


app = FastAPI()


@app.get("/")
def index():
    logging.info("at the index endpoint")
    return {"message": "Welcome to the Book API v0"}


@app.get("/books/{book_id}")
def get_book(book_id: uuid.UUID):
    return {}
