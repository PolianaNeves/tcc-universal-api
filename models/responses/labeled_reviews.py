from pydantic import BaseModel
from typing import List


class FrequentTerms(BaseModel):
    term: str
    frequency: str


class FrequentTermsList(BaseModel):
    data: List[FrequentTerms]


class ReviewsCount(BaseModel):
    count: int


class ReviewsCountByYear(ReviewsCount):
    year: str


class ReviewsCountByYearList(BaseModel):
    data: List[ReviewsCountByYear]


class ReviewsCountByBranch(ReviewsCount):
    branch: str


class ReviewsCountByBranchList(BaseModel):
    data: List[ReviewsCountByBranch]
