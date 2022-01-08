from pydantic import BaseModel
from typing import List


class FrequentTerms(BaseModel):
    term: str
    frequency: str


class FrequentTermsList(BaseModel):
    data: List[FrequentTerms]


class ReviewsCount(BaseModel):
    count: int
