from models.branches import ReviewsCountByBranch
from models.by_year import ReviewsCountByYear
from models.ratings import ReviewsCountByRating


def count_reviews_by_year(grouped_df):
    list_by_year = []
    for key, item in grouped_df:
        count_by_year = ReviewsCountByYear(year=str(key), count=len(item))
        list_by_year.append(count_by_year)
    return list_by_year


def count_reviews_by_branch(grouped_df):
    list_by_branch = []
    for key, item in grouped_df:
        count_by_branch = ReviewsCountByBranch(branch=key, count=len(item))
        list_by_branch.append(count_by_branch)
    return list_by_branch


def count_reviews_by_rating(grouped_df):
    list_by_rating = []
    for key, item in grouped_df:
        count_by_rating = ReviewsCountByRating(rating=key, count=len(item))
        list_by_rating.append(count_by_rating)
    return list_by_rating
