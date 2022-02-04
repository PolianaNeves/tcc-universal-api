from pydantic import BaseModel
from typing import List

from models.reviews import ReviewsCount


class ReviewsCountByBranch(BaseModel):
    label: str
    total: int
    positive: int
    negative: int


class ReviewsCountByBranchList(BaseModel):
    data: List[ReviewsCountByBranch]
