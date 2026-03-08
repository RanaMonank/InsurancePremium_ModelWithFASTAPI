from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):
    
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the User")]
    weight: Annotated[float, Field(..., description="weight of the User")]
    height: Annotated[float, Field(..., description="height of the User")]
    income_lpa: Annotated[float, Field(..., description="LPA of the User")]
    smoker: Annotated[bool, Field(..., description="is the User Smoker")]
    city: Annotated[str, Field(..., description="city of the User")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the User")]
    
    @field_validator('city')
    @classmethod
    def city_validation(cls, value):
        return value.strip().title()
    
    @computed_field(return_type=float)
    @property
    def bmi(self):
        return round(self.weight/(self.height**2), 2)
    
    @computed_field(return_type=str)
    @property
    def lifestyle_risk(self):
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field(return_type=str)
    @property
    def age_group(self):
        if self.age < 25:
            return "young"
        elif self.age < 50:
            return "adult"
        elif self.age < 60:
            return "middel_age"
        else:
            return "older"
    
    
    @computed_field(return_type=int)
    @property
    def city_tier(self):
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            3