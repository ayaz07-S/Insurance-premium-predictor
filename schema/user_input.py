from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities


class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="The age of the patient", example=30)]
    weight: Annotated[float, Field(..., gt=0, description="The weight of the patient in kilograms", example=70.5)]
    height: Annotated[float, Field(..., gt=0, description="The height of the patient in meters", example=1.75)]
    income_lpa: Annotated[float, Field(..., gt=0, description="The income of the patient in LPA", example=5.0)]
    smoker: Annotated[Literal["yes", "no"], Field(..., description="Whether the patient is a smoker or not", example="no")]
    city: Annotated[str, Field(..., description="The city where the patient lives", example="Mumbai")]
    occupation: Annotated[Literal["retired", "freelancer", "student", "government_job","business_owner", "unemployed","private_job"], Field(..., description="The occupation of the patient", example="business_owner")]

    @field_validator("city")
    def normalize_city(cls, value: str) -> str:
        return value.strip().title()


    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi >= 30:
            return "high"
        elif self.smoker or self.bmi >= 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 18:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle-aged"
        else:
            return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
