from fastapi import FastAPI, Path, HTTPException, Query
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
    # return {'error':'Invalid patient ID'}
    raise HTTPException(status_code=404, detail="Patient ID not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of age or bmi"),
    order: str = Query("asc", description="Sort in ascending or descending order")
):
    valid_fields = ["age", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Choose from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be 'asc' or 'desc'"
        )

    data = load_data()

    sorted_data = sorted(
        data["patients"],
        key=lambda x: x.get(sort_by, 0),
        reverse=(order == "desc")
    )

    return sorted_data