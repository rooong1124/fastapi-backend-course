from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/abc')
def read_abc():
    return '<p>114514<p>'