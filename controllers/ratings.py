from constants import POSITIVE, NEGATIVE
from controllers.utils import count_reviews_by_rating


def get_reviews_count_by_ratings(dataset):
    grouped_df = dataset.groupby(["rating"])
    return count_reviews_by_rating(grouped_df)


def get_reviews_count_filter_by_rating(dataset, rating):
    temp_dataset = dataset[dataset["rating"] == rating]
    return len(temp_dataset)


def get_positive_reviews_count_by_ratings(dataset):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    grouped_df = temp_dataset.groupby(["rating"])
    return count_reviews_by_rating(grouped_df)


def get_positive_reviews_count_filter_by_rating(dataset, rating):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    return get_reviews_count_filter_by_rating(temp_dataset, rating)


def get_negative_reviews_count_by_ratings(dataset):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    grouped_df = temp_dataset.groupby(["rating"])
    return count_reviews_by_rating(grouped_df)


def get_negative_reviews_count_filter_by_rating(dataset, rating):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    return get_reviews_count_filter_by_rating(temp_dataset, rating)
