from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount


class ReviewsCountByBranch(ReviewsCount):
    label: str


class ReviewsCountByBranchList(BaseModel):
    data: List[ReviewsCountByBranch]
