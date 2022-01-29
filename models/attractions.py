from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount


class ReviewsCountByAttraction(ReviewsCount):
    label: str


class ReviewsCountByAttractionList(BaseModel):
    data: List[ReviewsCountByAttraction]
