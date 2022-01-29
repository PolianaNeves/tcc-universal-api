from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount


class FrequentTerms(ReviewsCount):
    label: str


class FrequentTermsList(BaseModel):
    data: List[FrequentTerms]
