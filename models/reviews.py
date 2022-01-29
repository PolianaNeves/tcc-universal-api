from pydantic import BaseModel


class ReviewsCount(BaseModel):
    value: int
