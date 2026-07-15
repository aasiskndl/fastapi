from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional


class Patient(BaseModel):
    
    # name must be within 50 characters
    name: str = Field(max_length=50)
    
    # this checks that the values must be greater than 18 and less thatn 40 years
    age: int = Field(gt=18, lt=40)
    email: EmailStr
    url: AnyUrl
    weight: float = Field(gt=0) # this is the constraint that will check if the value is >0 or not 
    married: bool = False
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str]
    
def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    
    print("inserted")
    
patient_info = {'name':'Hari', 'age': 22, 'email':'hari@gmail.cpm', 'url':'https://aashish47.com.np', 'weight':89, 'married': False, 'allergies': ['pollen'], 'contact_details': {'phone':'9889239524'}}
patient1= Patient(**patient_info)

insert_data(patient1)