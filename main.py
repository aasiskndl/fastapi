from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Hello():
    return {'message':'Hello'}

@app.get("/about")
def about():
    return {'message': 'This is about section '}