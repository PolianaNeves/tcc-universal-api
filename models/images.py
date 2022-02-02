from pydantic import BaseModel


class ImageDecodedResponse(BaseModel):
    data: str