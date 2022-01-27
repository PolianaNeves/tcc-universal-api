from controllers.utils import count_reviews_by_attraction


def get_reviews_count_by_attraction(branch, label=""):
    column_filter = f'{branch}_count'
    if label != "":
        column_filter = f'{branch}_count_{label}'
    return count_reviews_by_attraction(column_filter)


def get_reviews_count_by_attraction(branch, label=""):
    column_filter = f'{branch}_count'
    if label != "":
        column_filter = f'{branch}_count_{label}'
    return count_reviews_by_attraction(column_filter)
