from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# create app
app = FastAPI()

#validation date
class Book(BaseModel):
    title:str
    author:str
    page:int
    editorial:Optional[str]


@app.get('/')
def first_read():
    return {'greetings':'Hello world¡¡'}

@app.get('/hello')
def hello_world():
    return {'hello':'world'}

# parameter router
@app.get('/books/{id}')
def show_book(id:int):
    return {'data':id}


@app.post('/books')
def insert_book(book:Book):
    return {'message':f"book {book.title} insert"}
