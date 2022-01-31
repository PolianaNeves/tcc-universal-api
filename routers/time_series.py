from fastapi import APIRouter, Response, Path, status
import os
import base64

from models.images import ImageDecodedResponse


my_path = os.path.relpath(os.path.join(os.path.dirname(__file__), os.pardir))
router = APIRouter()


@router.get("/reviews/time_series/{name}", response_model=ImageDecodedResponse)
async def default_time_series(response: Response,
                              name: str = Path(None, description="Time series name to be returned")):
    filename = f"{name}.jpeg"
    path = os.path.join("./assets", filename)
    if os.path.exists(path):
        b64_string = base64.b64encode(open(path, "rb").read())
        return ImageDecodedResponse(data=b64_string.decode('utf-8'))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response


@router.get("/reviews/time_series/{name}/details", response_model=ImageDecodedResponse)
async def time_series_details(response: Response,
                              name: str = Path(None, description="Time series name to be returned")):
    filename = f"{name}.jpeg"
    path = os.path.join("./assets/details", filename)
    if os.path.exists(path):
        b64_string = base64.b64encode(open(path, "rb").read())
        return ImageDecodedResponse(data=b64_string.decode('utf-8'))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
