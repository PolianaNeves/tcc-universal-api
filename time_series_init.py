from controllers.utils import parse_df, train_and_predict, plot_prediction
from init_dataset import dataset_completed
import os

PANDEMIC_YEAR = 2019
NEGATIVE = 0
POSITIVE = 1


if len(os.listdir('./assets')) == 0:
    """"Train the data with the full dataset, and preview the forecasting with the smaller groups/filters"""
    df_full_parsed = parse_df(dataset_completed.loc[dataset_completed["year"] <= 2019])
    plot_prediction(df_full_parsed, "default_prediction.png", 1)

    df_florida_reviews = dataset_completed.loc[(dataset_completed["branch"] == "Universal Studios Florida") & (dataset_completed["year"] <= 2019)]
    df_florida_reviews_parsed = parse_df(df_florida_reviews)
    plot_prediction(df_florida_reviews_parsed, "florida.png", 2)

    df_florida_neg_reviews = df_florida_reviews.loc[df_florida_reviews["label"] == NEGATIVE]
    df_florida_neg_reviews_parsed = parse_df(df_florida_neg_reviews)
    plot_prediction(df_florida_neg_reviews_parsed, "florida_neg.png", 3)

    df_florida_pos_reviews = df_florida_reviews.loc[df_florida_reviews["label"] == POSITIVE]
    df_florida_pos_reviews_parsed = parse_df(df_florida_pos_reviews)
    plot_prediction(df_florida_pos_reviews_parsed, "florida_pos.png", 4)

    df_japan_reviews = dataset_completed.loc[(dataset_completed["branch"] == "Universal Studios Japan") & (dataset_completed["year"] <= 2019)]
    df_japan_reviews_parsed = parse_df(df_japan_reviews)
    plot_prediction(df_japan_reviews_parsed, "japan.png", 5)

    df_japan_neg_reviews = df_japan_reviews.loc[df_japan_reviews["label"] == NEGATIVE]
    df_japan_neg_reviews_parsed = parse_df(df_japan_neg_reviews)
    plot_prediction(df_japan_neg_reviews_parsed, "japan_neg.png", 6)

    df_japan_pos_reviews = df_japan_reviews.loc[df_japan_reviews["label"] == POSITIVE]
    df_japan_pos_reviews_parsed = parse_df(df_japan_pos_reviews)
    plot_prediction(df_japan_pos_reviews_parsed, "japan_pos.png", 7)

    df_singapore_reviews = dataset_completed.loc[(dataset_completed["branch"] == "Universal Studios Singapore") & (dataset_completed["year"] <= 2019)]
    df_singapore_reviews_parsed = parse_df(df_singapore_reviews)
    plot_prediction(df_singapore_reviews_parsed, "singapore.png", 8)

    df_singapore_neg_reviews = df_singapore_reviews.loc[df_singapore_reviews["label"] == NEGATIVE]
    df_singapore_neg_reviews_parsed = parse_df(df_singapore_neg_reviews)
    plot_prediction(df_singapore_neg_reviews_parsed, "singapore_neg.png", 9)

    df_singapore_pos_reviews = df_singapore_reviews.loc[df_singapore_reviews["label"] == POSITIVE]
    df_singapore_pos_reviews_parsed = parse_df(df_singapore_pos_reviews)
    plot_prediction(df_singapore_pos_reviews_parsed, "singapore_pos.png", 10)
