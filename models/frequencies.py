from pydantic import BaseModel
from typing import List


class FrequentTerms(BaseModel):
    label: str
    value: float


class FrequentTermsList(BaseModel):
    data: List[FrequentTerms]
