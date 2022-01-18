import numpy as np

from constants import POSITIVE, NEGATIVE


def get_positive_reviews_count(dataset):
    temp_dataset = dataset[dataset["label"] == POSITIVE]
    return len(temp_dataset)


def get_negative_reviews_count(dataset):
    temp_dataset = dataset[dataset["label"] == NEGATIVE]
    return len(temp_dataset)
