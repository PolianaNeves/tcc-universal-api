import numpy as np

from controllers.utils import count_reviews_by_year

POSITIVE = 1
NEGATIVE = 0


def get_top_n_frequent_terms(dataset, top_n):
    temp_dataset = dataset.sort_values(by="frequency", ascending=False)
    temp_dataset.columns = ["term", "frequency"]
    return np.array(temp_dataset.head(top_n))


def get_reviews_count_by_year(dataset):
    grouped_df = dataset.groupby(["year"])
    return count_reviews_by_year(grouped_df)


def get_reviews_count_filter_by_year(dataset, year):
    temp_dataset = dataset[dataset["year"] == year]
    return len(temp_dataset)


def get_positive_reviews_count(dataset):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    return len(temp_dataset)


def get_positive_reviews_count_by_year(dataset):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    grouped_df = temp_dataset.groupby(["year"])
    return count_reviews_by_year(grouped_df)


def get_positive_reviews_count_filter_by_year(dataset, year):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    return get_reviews_count_filter_by_year(temp_dataset, year)


def get_negative_reviews_count(dataset):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    return len(temp_dataset)


def get_negative_reviews_count_by_year(dataset):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    grouped_df = temp_dataset.groupby(["year"])
    return count_reviews_by_year(grouped_df)


def get_negative_reviews_count_filter_by_year(dataset, year):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    return get_reviews_count_filter_by_year(temp_dataset, year)
