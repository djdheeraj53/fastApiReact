from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {
        'data': {
            'name': 'dheeraj'
        }
    }

@app.get('/blog')
def about(limit=10, publish: bool = True, sort: Optional[str] = None):
    if publish:
        return publish
    else:
        return {'data': f"blog list {limit} {publish}"}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return id

class Blog(BaseModel):
    pass

@app.post('/blog')
def create_blog():
    return {'data': 'blog created'}