from pydantic import BaseModel
from typing import List, Dict, Optional

# this is all for type validation (to check if the data types are valid or not) 
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    # married: bool
    married: bool = False # this sets the married value default as false
    # allergies: Optional[List[str]] this makes the field optional
    allergies: Optional[List[str]] = None # this also makes the field optional but with default value as null
    contact_details: Dict[str, str]
    
def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    
    print("inserted")
    
patient_info = {'name':'Hari', 'age': 32, 'weight':89, 'married': False, 'allergies': ['pollen'], 'contact_details': {'email':'hari@gmail.com', 'phone':'9889239524'}}
patient1= Patient(**patient_info)

insert_data(patient1)