from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['domain.com', 'icici.com']
        domain_name= value.split('@')[-1]
        #this split function splits the text into two parts from @ for eg: if there is abc@gmail.com as email then it splits from @ and then returns 2 strings as 'abc' and 'gmail.com' and then [-1] in the code returns the value that is at the last of the string i.e. 'gmail.com'
        
        if domain_name not in valid_domains:
            raise ValueError('not in valid domain ')
        return value
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
    
patient_info = {
    'name':'Alen', 
    'email':'abc@doman.com', 
    'age': 24, 
    'weight':89, 
    'married': True, 
    'allergies': ['dust', 'pollen'], 'contact_details':{'phone':'85024895'}}
    
patient1 = Patient(**patient_info)
    
update_patient_data(patient1)
    
    