from fastapi import APIRouter, Path

from inits.init_dataset import dataset_completed
from models.branches import ReviewsCountByBranchList, ReviewsCountByBranch
from controllers import branches

router = APIRouter()


@router.get("/reviews/count/by/branch", response_model=ReviewsCountByBranchList)
async def count_reviews_by_branch():
    by_branch = branches.get_reviews_count_by_branch(dataset_completed)
    return ReviewsCountByBranchList(data=by_branch)


@router.get("/reviews/count/by/branch/{branch}", response_model=ReviewsCountByBranch)
async def count_reviews_by_branch(branch: str = Path(None, description="Branch to filter reviews")):
    count_by_branch = branches.get_reviews_count_filter_by_branch(dataset_completed, branch)
    return ReviewsCountByBranch(branch=branch, count=count_by_branch)


@router.get("/reviews/positive/count/by/branch", response_model=ReviewsCountByBranchList)
async def count_positive_reviews_by_branch():
    reviews_by_year = branches.get_positive_reviews_count_by_branch(dataset_completed)
    return ReviewsCountByBranchList(data=reviews_by_year)


@router.get("/reviews/positive/count/by/branch/{branch}", response_model=ReviewsCountByBranch)
async def count_positive_reviews_by_branch(branch: str = Path(None, description="Branch to filter reviews")):
    count_by_branch = branches.get_positive_reviews_count_filter_by_branch(dataset_completed, branch)
    return ReviewsCountByBranch(branch=branch, count=count_by_branch)


@router.get("/reviews/negative/count/by/branch", response_model=ReviewsCountByBranchList)
async def count_negative_reviews_by_branch():
    reviews_by_branch = branches.get_negative_reviews_count_by_branch(dataset_completed)
    return ReviewsCountByBranchList(data=reviews_by_branch)


@router.get("/reviews/negative/count/by/branch/{branch}", response_model=ReviewsCountByBranch)
async def count_negative_reviews_by_branch(branch: str = Path(None, description="Branch to filter the reviews")):
    count_by_branch = branches.get_negative_reviews_count_filter_by_branch(dataset_completed, branch)
    return ReviewsCountByBranch(count=count_by_branch, branch=branch)
