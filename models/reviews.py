from pydantic import BaseModel


class ReviewsCount(BaseModel):
    count: int
