from pydantic import BaseModel
from typing import List


class FrequentTermsResponse(BaseModel):
    term: str
    frequency: str


class FrequentTermsListResponse(BaseModel):
    data: List[FrequentTermsResponse]


class ReviewsCount(BaseModel):
    count: int


class ReviewsCountByYear(ReviewsCount):
    year: str


class ReviewsCountByYearResponse(BaseModel):
    data: List[ReviewsCountByYear]
