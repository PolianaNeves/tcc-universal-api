from fastapi import APIRouter, Path

from models.attractions import ReviewsCountByAttractionList
from enums.attractions_enums import BranchName, LabelName
from controllers import attractions

router = APIRouter()


@router.get("/reviews/count/by/{branch}/attraction", response_model=ReviewsCountByAttractionList)
async def reviews_count_by_attractions(branch: BranchName = Path(None, description="Branch to filter reviews")):
    by_attraction = attractions.get_reviews_count_by_attraction(branch=branch)
    return ReviewsCountByAttractionList(data=by_attraction)


@router.get("/reviews/count/{label}/by/{branch}/attraction", response_model=ReviewsCountByAttractionList)
async def reviews_count_by_attractions(branch: BranchName = Path(None, description="Branch to filter reviews"),
                                       label: LabelName = Path(None, description="Filter by positive or negative "
                                                                                 "reviews")):
    by_attraction = attractions.get_reviews_count_by_attraction(branch=branch, label=label)
    return ReviewsCountByAttractionList(data=by_attraction)
