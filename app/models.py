from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    userId: str = Field(..., description="userId is required")

    # class Config:
    #     arbitrary_types_allowed = True
