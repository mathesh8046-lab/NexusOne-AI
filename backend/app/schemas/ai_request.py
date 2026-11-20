
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AIRequestCreate(BaseModel):
    domain: str = Field(min_length=1, max_length=50)
    input_text: str = Field(min_length=1)


class AIRequestResponse(BaseModel):
    id: int
    user_id: int
    domain: str
    input_text: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AIRequestStatusUpdate(BaseModel):
    status: Literal[
        "pending",
        "processing",
        "completed",
        "failed"
    ]
