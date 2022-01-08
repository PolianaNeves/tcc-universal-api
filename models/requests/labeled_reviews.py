from pydantic import BaseModel


class FrequentTermsRequest(BaseModel):
    top_n: int
