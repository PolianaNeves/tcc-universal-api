from controllers.utils import parse_df, train_and_predict, plot_prediction, train_with_prophet_model, \
    predict_with_prophet_model
from inits.init_dataset import dataset_completed
import os

if len(os.listdir('./assets')) == 1 or len(os.listdir('./assets/details')) == 1:
    df_full_parsed = parse_df(dataset_completed.loc[dataset_completed["year"] <= constants.PANDEMIC_YEAR])

    df_florida_reviews = dataset_completed.loc[(dataset_completed["branch"] == constants.FLORIDA_BRANCH) & (
                dataset_completed["year"] <= constants.PANDEMIC_YEAR)]
    df_florida_reviews_parsed = parse_df(df_florida_reviews)

    df_florida_neg_reviews = df_florida_reviews.loc[df_florida_reviews["label"] == constants.NEGATIVE]
    df_florida_neg_reviews_parsed = parse_df(df_florida_neg_reviews)

    df_florida_pos_reviews = df_florida_reviews.loc[df_florida_reviews["label"] == constants.POSITIVE]
    df_florida_pos_reviews_parsed = parse_df(df_florida_pos_reviews)

    df_japan_reviews = dataset_completed.loc[(dataset_completed["branch"] == constants.JAPAN_BRANCH) & (
                dataset_completed["year"] <= constants.PANDEMIC_YEAR)]
    df_japan_reviews_parsed = parse_df(df_japan_reviews)

    df_japan_neg_reviews = df_japan_reviews.loc[df_japan_reviews["label"] == constants.NEGATIVE]
    df_japan_neg_reviews_parsed = parse_df(df_japan_neg_reviews)

    df_japan_pos_reviews = df_japan_reviews.loc[df_japan_reviews["label"] == constants.POSITIVE]
    df_japan_pos_reviews_parsed = parse_df(df_japan_pos_reviews)

    df_singapore_reviews = dataset_completed.loc[(dataset_completed["branch"] == constants.SINGAPORE_BRANCH) & (
                dataset_completed["year"] <= constants.PANDEMIC_YEAR)]
    df_singapore_reviews_parsed = parse_df(df_singapore_reviews)

    df_singapore_neg_reviews = df_singapore_reviews.loc[df_singapore_reviews["label"] == constants.NEGATIVE]
    df_singapore_neg_reviews_parsed = parse_df(df_singapore_neg_reviews)

    df_singapore_pos_reviews = df_singapore_reviews.loc[df_singapore_reviews["label"] == constants.POSITIVE]
    df_singapore_pos_reviews_parsed = parse_df(df_singapore_pos_reviews)

    if len(os.listdir('./assets')) == 1:
        plot_prediction(df_full_parsed, constants.DEFAULT_FILE, 1)
        plot_prediction(df_florida_reviews_parsed, constants.FLORIDA_FILE, 2)
        plot_prediction(df_florida_neg_reviews_parsed, constants.FLORIDA_NEG_FILE, 3)
        plot_prediction(df_florida_pos_reviews_parsed, constants.FLORIDA_POS_FILE, 4)
        plot_prediction(df_japan_reviews_parsed, constants.JAPAN_FILE, 5)
        plot_prediction(df_japan_neg_reviews_parsed, constants.JAPAN_NEG_FILE, 6)
        plot_prediction(df_japan_pos_reviews_parsed, constants.JAPAN_POS_FILE, 7)
        plot_prediction(df_singapore_reviews_parsed, constants.SINGAPORE_FILE, 8)
        plot_prediction(df_singapore_neg_reviews_parsed, constants.SINGAPORE_NEG_FILE, 9)
        plot_prediction(df_singapore_pos_reviews_parsed, constants.SINGAPORE_POS_FILE, 10)

    if len(os.listdir('./assets/details')) == 1:
        prophet_full_df = train_with_prophet_model(df_full_parsed)
        predict_with_prophet_model(prophet_full_df, constants.DEFAULT_FILE)

        prophet_florida_df = train_with_prophet_model(df_florida_reviews_parsed)
        predict_with_prophet_model(prophet_florida_df, constants.FLORIDA_FILE)

        prophet_florida_neg_df = train_with_prophet_model(df_florida_neg_reviews_parsed)
        predict_with_prophet_model(prophet_florida_neg_df, constants.FLORIDA_NEG_FILE)

        prophet_florida_pos_df = train_with_prophet_model(df_florida_pos_reviews_parsed)
        predict_with_prophet_model(prophet_florida_pos_df, constants.FLORIDA_POS_FILE)

        prophet_japan_df = train_with_prophet_model(df_japan_reviews_parsed)
        predict_with_prophet_model(prophet_japan_df, constants.JAPAN_FILE)

        prophet_japan_neg_df = train_with_prophet_model(df_japan_neg_reviews_parsed)
        predict_with_prophet_model(prophet_japan_neg_df, constants.JAPAN_NEG_FILE)

        prophet_japan_pos_df = train_with_prophet_model(df_japan_pos_reviews_parsed)
        predict_with_prophet_model(prophet_japan_pos_df, constants.JAPAN_POS_FILE)

        prophet_singapore_df = train_with_prophet_model(df_singapore_reviews_parsed)
        predict_with_prophet_model(prophet_singapore_df, constants.SINGAPORE_FILE)

        prophet_singapore_neg_df = train_with_prophet_model(df_singapore_neg_reviews_parsed)
        predict_with_prophet_model(prophet_singapore_neg_df, constants.SINGAPORE_NEG_FILE)

        prophet_singapore_pos_df = train_with_prophet_model(df_singapore_pos_reviews_parsed)
        predict_with_prophet_model(prophet_singapore_pos_df, constants.SINGAPORE_POS_FILE)
