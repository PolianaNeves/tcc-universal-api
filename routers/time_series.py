from fastapi import APIRouter, Response, Path, status
from fastapi.responses import FileResponse
import os


my_path = os.path.relpath(os.path.join(os.path.dirname(__file__), os.pardir))
router = APIRouter()


@router.get("/reviews/time_series/{name}", response_class=FileResponse)
async def default_time_series(response: Response,
                              name: str = Path(None, description="Time series name to be returned")):
    filename = f"{name}.png"
    path = os.path.join("./assets", filename)
    if os.path.exists(path):
        return FileResponse(path)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response


@router.get("/reviews/time_series/{name}/details", response_class=FileResponse)
async def time_series_details(response: Response,
                              name: str = Path(None, description="Time series name to be returned")):
    filename = f"{name}.png"
    path = os.path.join("./assets/details", filename)
    if os.path.exists(path):
        return FileResponse(path)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
