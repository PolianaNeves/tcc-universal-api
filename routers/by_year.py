from fastapi import APIRouter, Path

from inits.init_dataset import dataset_completed
from models.by_year import ReviewsCountByYearList, ReviewsCountByYear
from controllers import by_year

router = APIRouter()


@router.get("/reviews/count/by/year", response_model=ReviewsCountByYearList)
async def count_positive_reviews_by_year():
    reviews_by_year = by_year.get_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearList(data=reviews_by_year)


@router.get("/reviews/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_positive_reviews_by_year(year: int = Path(None, description="Year to routerlied to the filter")):
    count_by_year = by_year.get_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))


@router.get("/reviews/positive/count/by/year", response_model=ReviewsCountByYearList)
async def count_positive_reviews_by_year():
    reviews_by_year = by_year.get_positive_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearList(data=reviews_by_year)


@router.get("/reviews/positive/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_positive_reviews_by_year(year: int = Path(None, description="Year to routerlied to the filter")):
    count_by_year = by_year.get_positive_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))


@router.get("/reviews/negative/count/by/year", response_model=ReviewsCountByYearList)
async def count_negative_reviews_by_year():
    reviews_by_year = by_year.get_negative_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearList(data=reviews_by_year)


@router.get("/reviews/negative/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_negative_reviews_by_year(year: int = Path(None, description="Year to routerlied to the filter")):
    count_by_year = by_year.get_negative_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))
