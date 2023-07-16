import uuid
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    task: str = Field(...)

    class Config:
        allow_population_by_field_name = True
