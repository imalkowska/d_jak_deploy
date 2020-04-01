# main.py

from fastapi import FastAPI 

from pydantic import BaseModel

app = FastAPI()
# to see what funny will come
app.counter = 0

class HelloResp(BaseModel):
    msg: str

@app.get("/")
def root():
	return {"message": "Hello World"}


#@app.get("/hello/{name}")
#async def read_item(name: str):
#	return f"Hello {name}"

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)


@app.get("/hello/{name}", response_model=HelloResp)
async def read_item(name: str):
    return HelloResp(msg=f'"Hello {name}"')


class GiveMeSomethingRq(BaseModel):
    first_key: str


class GiveMeSomethingResp(BaseModel):
    received: dict
    constant_data: str = "python jest super"


@app.post("/dej/mi/cos", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
    return GiveMeSomethingResp(received=rq.dict())