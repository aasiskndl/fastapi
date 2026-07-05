from fastapi import FastAPI, Path
import json 
app = FastAPI()

def load_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def Hello():
    return {'message':'Hello this is the main page'}

@app.get("/about")
def about():
    return {'message': 'This is about section '}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patients/{patient_id}")
def view_patient(patient_id:int = Path(..., description="ID of patient in the DB", example="1")):
    # load all the patents data
    data = load_data()
    patients = data['patients']
    
    for patient in patients:
        if patient['id'] == patient_id:
            return patient
    return {'error':'Invalid patient ID'}

    