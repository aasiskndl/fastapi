from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

import json

app = FastAPI()

class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description="ID of the patient", examples=['01'])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description='Name of the city patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['Male', 'Female', 'Others'], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in Meters')]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in KG")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi <25:
            return 'Normal'
        elif self.bmi <30:
            return 'Normal'
        else:
            return 'Obese'
        
        
def load_data():
    with open('data1.json', 'r') as f:
        data = json.load(f)
        
    return data


@app.get('/')
def hello():
    return {'message': 'Patient Management System'}


@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    
    # load the data
    data = load_data()
    
    #check if the patient already exists in the database
    if patient.id in data:
        return HTTPException(status_code=400, detail="Patient already exists")
    
    
    #if the patient data does not exist in the database, then add the new patients data
    data[patient.id] = patient.model_dump(exclude=["id"])
    
    


    