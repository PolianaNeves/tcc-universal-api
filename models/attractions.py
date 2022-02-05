from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount, ReviewsCountBy


class ReviewsCountByAttraction(ReviewsCount):
    label: str


class ReviewsCountByAttractionList(BaseModel):
    data: List[ReviewsCountByAttraction]


class ReviewsCountAttractionsByBranch(BaseModel):
    branch: str
    data: List[ReviewsCountBy]


class ReviewsCountAttractionsByBranchList(BaseModel):
    data: List[ReviewsCountAttractionsByBranch]
