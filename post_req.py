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
        
        
        
    