from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    
    # name must be within 50 characters
    #name: str = Field(max_length=50)
    
    # we can use Annotated to add the metadata to the field
    name: Annotated[str, Field(max_length=50, title='Name of patient', description="Give the name of the patient within 50 characters", examples=['hari', 'amit'])]
    
    # this checks that the values must be greater than 18 and less thatn 40 years
    age: int = Field(gt=18, lt=40)
    email: EmailStr
    url: AnyUrl
    
    #the weight will be inserted without any problem if it is passed as a string and it can cause problem if we need to do operation with this value , so to explicitly check if it is string or not we use Annotation 
    #weight: float = Field(gt=0)  this is the constraint that will check if the value is >0 or not 
    
    weight: Annotated[float, Field(gt=0, strict=True)]
    #(this strict = True checks if the value is of float or not) 
    
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