from pydantic import BaseModel
from typing import List


class ReviewsCount(BaseModel):
    value: int


class ReviewsCountBy(BaseModel):
    label: str
    total: int
    positive: int
    negative: int


class ReviewsGroup(BaseModel):
    key: str
    data: List[ReviewsCountBy]


class ReviewsGroupList(BaseModel):
    data: List[ReviewsGroup]


class ReviewsCountByList(BaseModel):
    data: List[ReviewsCountBy]