from fastapi import FastAPI
import json 
app = FastAPI()

def load_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def Hello():
    return {'message':'Hello'}

@app.get("/about")
def about():
    return {'message': 'This is about section '}

@app.get("/view")
def view():
    data = load_data()
    return data