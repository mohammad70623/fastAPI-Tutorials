from fastapi import FastAPI
from pydantic import BaseModel, computed_field, Field 
from typing import Literal, Annotated
import pickle 
import pandas as pd

#import the ML model 
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

#pudantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='height of the user')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual salary in LPA' )]
    smoker: Annotated[bool, Field(..., description='is user is smoker')]
    city:  Annotated[str, Field(..., description='the city of users belongs to')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the users')]

    @computed_field
    @property
    def bmi(self) ->float:
        return round(self.weight/(self.height**2), 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi >27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age <45:
            return "Adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    





    