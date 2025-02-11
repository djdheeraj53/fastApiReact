from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

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
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return blog


# debugging purpose
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)