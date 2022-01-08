from fastapi import APIRouter, Path
from controllers import ratings
from init_dataset import dataset_completed
from models.ratings import ReviewsCountByRatingsList, ReviewsCountByRating

router = APIRouter()


@router.get("/reviews/count/by/ratings", response_model=ReviewsCountByRatingsList)
async def count_reviews_by_ratings():
    by_ratings = ratings.get_reviews_count_by_ratings(dataset_completed)
    return ReviewsCountByRatingsList(data=by_ratings)


@router.get("/reviews/count/by/ratings/{rating}", response_model=ReviewsCountByRating)
async def count_reviews_by_rating(rating: float = Path(None, description="Rating to filter reviews")):
    count_by_rating = ratings.get_reviews_count_filter_by_rating(dataset_completed, rating)
    return ReviewsCountByRating(rating=rating, count=count_by_rating)


@router.get("/reviews/positive/count/by/ratings", response_model=ReviewsCountByRatingsList)
async def count_positive_reviews_by_ratings():
    by_ratings = ratings.get_positive_reviews_count_by_ratings(dataset_completed)
    return ReviewsCountByRatingsList(data=by_ratings)


@router.get("/reviews/positive/count/by/ratings/{rating}", response_model=ReviewsCountByRating)
async def count_positive_reviews_by_rating(rating: float = Path(None, description="Rating to filter reviews")):
    count_by_rating = ratings.get_positive_reviews_count_filter_by_rating(dataset_completed, rating)
    return ReviewsCountByRating(rating=rating, count=count_by_rating)


@router.get("/reviews/negative/count/by/ratings", response_model=ReviewsCountByRatingsList)
async def count_negative_reviews_by_ratings():
    by_ratings = ratings.get_negative_reviews_count_by_ratings(dataset_completed)
    return ReviewsCountByRatingsList(data=by_ratings)


@router.get("/reviews/negative/count/by/ratings/{rating}", response_model=ReviewsCountByRating)
async def count_negative_reviews_by_rating(rating: float = Path(None, description="Rating to filter reviews")):
    count_by_rating = ratings.get_negative_reviews_count_filter_by_rating(dataset_completed, rating)
    return ReviewsCountByRating(rating=rating, count=count_by_rating)
