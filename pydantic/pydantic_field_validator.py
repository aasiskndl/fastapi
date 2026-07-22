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
    
    # this is used to return the value in uppercase 
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode= 'after')  # this is 'after' by default wew can change it 
    # the main functionality is that it automatically type converts it before performing any operation 
    #mode="before": Runs the validator before Pydantic validates or type-converts the input.
    #mode="after": Runs the validator after Pydantic validates and type-converts the input.
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
    
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
    
patient_info = {
    'name':'Alen', 
    'email':'abc@domain.com', 
    'age': 24, 
    'weight':89, 
    'married': True, 
    'allergies': ['dust', 'pollen'], 'contact_details':{'phone':'85024895'}}
    
patient1 = Patient(**patient_info)
    
update_patient_data(patient1)
    
    