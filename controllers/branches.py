from controllers import POSITIVE, NEGATIVE
from controllers.utils import count_reviews_by_branch


def get_reviews_count_by_branch(dataset):
    grouped_df = dataset.groupby(["branch"])
    return count_reviews_by_branch(grouped_df)


def get_reviews_count_filter_by_branch(dataset, branch):
    temp_dataset = dataset[dataset["branch"] == branch]
    return len(temp_dataset)


def get_positive_reviews_count_by_branch(dataset):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    grouped_df = temp_dataset.groupby(["branch"])
    return count_reviews_by_branch(grouped_df)


def get_positive_reviews_count_filter_by_branch(dataset, branch):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    return get_reviews_count_filter_by_branch(temp_dataset, branch)


def get_negative_reviews_count_by_branch(dataset):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    grouped_df = temp_dataset.groupby(["branch"])
    return count_reviews_by_branch(grouped_df)


def get_negative_reviews_count_filter_by_branch(dataset, branch):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    return get_reviews_count_filter_by_branch(temp_dataset, branch)