from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount


class ReviewsCountByRating(ReviewsCount):
    rating: float


class ReviewsCountByRatingsList(BaseModel):
    data: List[ReviewsCountByRating]
