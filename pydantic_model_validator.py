from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    
    name:str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact')
        return model 

   
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
    
patient_info = {
    'name':'Alen', 
    'email':'abc@domain.com', 
    'age': 84, 
    'weight':89, 
    'married': True, 
    'allergies': ['dust', 'pollen'], 
    'contact_details':{'phone':'85024895', 'emergency':'98320'}}
    
    
patient1 = Patient(**patient_info)
    
update_patient_data(patient1)