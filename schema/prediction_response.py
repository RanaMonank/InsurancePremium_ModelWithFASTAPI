from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    prediction_category: str = Field(..., description="The Predicted Insurance Premium Category", example="High")
    confidence: float = Field(..., description="Model's confidence score for the predicted class (range 0 to 1)",example=0.8432)
    class_probabilities: Dict[str, float] = Field(...,description="Probability distribution across all possible classed",example={'Low':0.15,"Medium":0.15,"High": 0.8432})