from fastapi import APIRouter, Path

from inits.init_dataset import dataset_completed
from models.branches import ReviewsCountByBranchList
from controllers import branches, utils

router = APIRouter()


@router.get("/reviews/count/by/branch", response_model=ReviewsCountByBranchList)
async def count_reviews_by_branch():
    by_branch = utils.get_reviews_count_by_branch(dataset_completed)
    return ReviewsCountByBranchList(data=by_branch)
