from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount


class ReviewsCountByAttraction(ReviewsCount):
    attraction: str


class ReviewsCountByAttractionList(BaseModel):
    data: List[ReviewsCountByAttraction]
