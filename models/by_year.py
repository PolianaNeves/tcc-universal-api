from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount


class ReviewsCountByYear(ReviewsCount):
    year: str


class ReviewsCountByYearList(BaseModel):
    data: List[ReviewsCountByYear]
