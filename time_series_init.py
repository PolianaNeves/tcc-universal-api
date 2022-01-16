from controllers.utils import parse_df, train_and_predict, plot_prediction, train_with_prophet_model, \
    predict_with_prophet_model
from init_dataset import dataset_completed
import os

PANDEMIC_YEAR = 2019
NEGATIVE = 0
POSITIVE = 1

if len(os.listdir('./assets')) == 1 or len(os.listdir('./assets/details')) == 1:
    df_full_parsed = parse_df(dataset_completed.loc[dataset_completed["year"] <= PANDEMIC_YEAR])

    df_florida_reviews = dataset_completed.loc[(dataset_completed["branch"] == "Universal Studios Florida") & (dataset_completed["year"] <= PANDEMIC_YEAR)]
    df_florida_reviews_parsed = parse_df(df_florida_reviews)

    df_florida_neg_reviews = df_florida_reviews.loc[df_florida_reviews["label"] == NEGATIVE]
    df_florida_neg_reviews_parsed = parse_df(df_florida_neg_reviews)

    df_florida_pos_reviews = df_florida_reviews.loc[df_florida_reviews["label"] == POSITIVE]
    df_florida_pos_reviews_parsed = parse_df(df_florida_pos_reviews)

    df_japan_reviews = dataset_completed.loc[(dataset_completed["branch"] == "Universal Studios Japan") & (dataset_completed["year"] <= PANDEMIC_YEAR)]
    df_japan_reviews_parsed = parse_df(df_japan_reviews)

    df_japan_neg_reviews = df_japan_reviews.loc[df_japan_reviews["label"] == NEGATIVE]
    df_japan_neg_reviews_parsed = parse_df(df_japan_neg_reviews)

    df_japan_pos_reviews = df_japan_reviews.loc[df_japan_reviews["label"] == POSITIVE]
    df_japan_pos_reviews_parsed = parse_df(df_japan_pos_reviews)

    df_singapore_reviews = dataset_completed.loc[(dataset_completed["branch"] == "Universal Studios Singapore") & (dataset_completed["year"] <= PANDEMIC_YEAR)]
    df_singapore_reviews_parsed = parse_df(df_singapore_reviews)

    df_singapore_neg_reviews = df_singapore_reviews.loc[df_singapore_reviews["label"] == NEGATIVE]
    df_singapore_neg_reviews_parsed = parse_df(df_singapore_neg_reviews)

    df_singapore_pos_reviews = df_singapore_reviews.loc[df_singapore_reviews["label"] == POSITIVE]
    df_singapore_pos_reviews_parsed = parse_df(df_singapore_pos_reviews)

    if len(os.listdir('./assets')) == 1:
        plot_prediction(df_full_parsed, "default_prediction.png", 1)
        plot_prediction(df_florida_reviews_parsed, "florida.png", 2)
        plot_prediction(df_florida_neg_reviews_parsed, "florida_neg.png", 3)
        plot_prediction(df_florida_pos_reviews_parsed, "florida_pos.png", 4)
        plot_prediction(df_japan_reviews_parsed, "japan.png", 5)
        plot_prediction(df_japan_neg_reviews_parsed, "japan_neg.png", 6)
        plot_prediction(df_japan_pos_reviews_parsed, "japan_pos.png", 7)
        plot_prediction(df_singapore_reviews_parsed, "singapore.png", 8)
        plot_prediction(df_singapore_neg_reviews_parsed, "singapore_neg.png", 9)
        plot_prediction(df_singapore_pos_reviews_parsed, "singapore_pos.png", 10)

    if len(os.listdir('./assets/details')) == 1:
        prophet_full_df = train_with_prophet_model(df_full_parsed)
        predict_with_prophet_model(prophet_full_df, "default_prediction.png")

        prophet_florida_df = train_with_prophet_model(df_florida_reviews_parsed)
        predict_with_prophet_model(prophet_florida_df, "florida.png")

        prophet_florida_neg_df = train_with_prophet_model(df_florida_neg_reviews_parsed)
        predict_with_prophet_model(prophet_florida_neg_df, "florida_neg.png")

        prophet_florida_pos_df = train_with_prophet_model(df_florida_pos_reviews_parsed)
        predict_with_prophet_model(prophet_florida_pos_df, "florida_pos.png")

        prophet_japan_df = train_with_prophet_model(df_japan_reviews_parsed)
        predict_with_prophet_model(prophet_japan_df, "japan.png")

        prophet_japan_neg_df = train_with_prophet_model(df_japan_neg_reviews_parsed)
        predict_with_prophet_model(prophet_japan_neg_df, "japan_neg.png")

        prophet_japan_pos_df = train_with_prophet_model(df_japan_pos_reviews_parsed)
        predict_with_prophet_model(prophet_japan_pos_df, "japan_pos.png")

        prophet_singapore_df = train_with_prophet_model(df_singapore_reviews_parsed)
        predict_with_prophet_model(prophet_singapore_df, "singapore.png")

        prophet_singapore_neg_df = train_with_prophet_model(df_singapore_neg_reviews_parsed)
        predict_with_prophet_model(prophet_singapore_neg_df, "singapore_neg.png")

        prophet_singapore_pos_df = train_with_prophet_model(df_singapore_pos_reviews_parsed)
        predict_with_prophet_model(prophet_singapore_pos_df, "singapore_pos.png")
