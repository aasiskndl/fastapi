from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    url: AnyUrl
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str]
    
def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    
    print("inserted")
    
patient_info = {'name':'Hari', 'age': 32, 'email':'hari@gmail.cpm', 'url':'https://aashish47.com.np', 'weight':89, 'married': False, 'allergies': ['pollen'], 'contact_details': {'phone':'9889239524'}}
patient1= Patient(**patient_info)

insert_data(patient1)