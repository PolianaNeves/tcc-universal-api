import numpy as np

from controllers import POSITIVE, NEGATIVE


def get_top_n_frequent_terms(dataset, top_n):
    temp_dataset = dataset.sort_values(by="frequency", ascending=False)
    temp_dataset.columns = ["term", "frequency"]
    return np.array(temp_dataset.head(top_n))


def get_positive_reviews_count(dataset):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    return len(temp_dataset)


def get_negative_reviews_count(dataset):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    return len(temp_dataset)
