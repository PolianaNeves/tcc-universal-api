from constants import POSITIVE, NEGATIVE, DEFAULT_BRANCH, FLORIDA_BRANCH, JAPAN_BRANCH, SINGAPORE_BRANCH
from models.branches import ReviewsCountByBranch

def get_reviews_count_by_branch(dataset):
    df_full_pos = dataset[dataset["label"] == POSITIVE]
    df_full_neg = dataset[dataset["label"] == NEGATIVE]
    df_florida = dataset[dataset["branch"] == FLORIDA_BRANCH]
    df_florida_pos = df_florida[df_florida["label"] == POSITIVE]
    df_florida_neg = df_florida[df_florida["label"] == NEGATIVE]
    df_japan = dataset[dataset["branch"] == JAPAN_BRANCH]
    df_japan_pos = df_japan[df_japan["label"] == POSITIVE]
    df_japan_neg = df_japan[df_japan["label"] == NEGATIVE]
    df_singapore = dataset[dataset["branch"] == SINGAPORE_BRANCH]
    df_singapore_pos = df_singapore[df_singapore["label"] == POSITIVE]
    df_singapore_neg = df_singapore[df_singapore["label"] == NEGATIVE]

    list_reviews = []
    list_reviews.append(ReviewsCountByBranch(label=DEFAULT_BRANCH,
        total=len(dataset), positive=len(df_full_pos), negative=len(df_full_neg)))
    list_reviews.append(ReviewsCountByBranch(label=FLORIDA_BRANCH, 
        total=len(df_florida), positive=len(df_florida_pos), negative=len(df_florida_neg)))
    list_reviews.append(ReviewsCountByBranch(label=JAPAN_BRANCH, 
        total=len(df_japan), positive=len(df_japan_pos), negative=len(df_japan_neg)))
    list_reviews.append(ReviewsCountByBranch(label=SINGAPORE_BRANCH, 
        total=len(df_singapore), positive=len(df_singapore_pos), negative=len(df_singapore_neg)))
    return list_reviews