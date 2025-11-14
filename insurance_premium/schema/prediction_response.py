from pydantic import BaseModel, Field
from  typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="the predicted insurance premium category",
        example ="high"
    )
    confidence: float =Field(
        ...,
        description="model's confidence score for the preadicted class (range: 0 to 1)",
        example= 0.8432
    )
    class_probabilities: Dict[str,float]= Field(
        ...,
        description= " Pobability distrbution ",
        example= {"low":0.01,"medium":0.15, "high":0.84},
    )