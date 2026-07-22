from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    
def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")
    
patient_info = {'name':'Hari', 'age': 32}
patient1= Patient(**patient_info)

insert_data(patient1)