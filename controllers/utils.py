from models.responses.labeled_reviews import ReviewsCountByYear


def count_reviews_by_year(grouped_df):
    list_by_year = []
    for key, item in grouped_df:
        count_by_year = ReviewsCountByYear(year=str(key), count=len(item))
        list_by_year.append(count_by_year)
    return list_by_year
