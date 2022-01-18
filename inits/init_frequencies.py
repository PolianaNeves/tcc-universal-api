import constants
from controllers import frequencies
from inits.init_dataset import dataset_completed
import os

TOP_N = 100

if len(os.listdir('./assets/wordcloud')) == 1:
    frequencies.generate_wordcloud(dataset_completed, TOP_N, constants.DEFAULT_FILE)

    positive_df = dataset_completed.loc[dataset_completed["label"] == constants.POSITIVE]
    frequencies.generate_wordcloud(positive_df, TOP_N, constants.DEFAULT_POS_FILE)

    negative_df = dataset_completed.loc[dataset_completed["label"] == constants.NEGATIVE]
    frequencies.generate_wordcloud(negative_df, TOP_N, constants.DEFAULT_NEG_FILE)

    florida_df = dataset_completed.loc[dataset_completed["branch"] == constants.FLORIDA_BRANCH]
    frequencies.generate_wordcloud(florida_df, TOP_N, constants.FLORIDA_FILE)

    florida_pos_df = positive_df.loc[positive_df["branch"] == constants.FLORIDA_BRANCH]
    frequencies.generate_wordcloud(florida_pos_df, TOP_N, constants.FLORIDA_POS_FILE)

    florida_neg_df = negative_df.loc[negative_df["branch"] == constants.FLORIDA_BRANCH]
    frequencies.generate_wordcloud(florida_neg_df, TOP_N, constants.FLORIDA_NEG_FILE)

    japan_df = dataset_completed.loc[dataset_completed["branch"] == constants.JAPAN_BRANCH]
    frequencies.generate_wordcloud(japan_df, TOP_N, constants.JAPAN_FILE)

    japan_pos_df = positive_df.loc[positive_df["branch"] == constants.JAPAN_BRANCH]
    frequencies.generate_wordcloud(japan_pos_df, TOP_N, constants.JAPAN_POS_FILE)

    japan_neg_df = negative_df.loc[negative_df["branch"] == constants.JAPAN_BRANCH]
    frequencies.generate_wordcloud(japan_neg_df, TOP_N, constants.JAPAN_NEG_FILE)

    singapore_df = dataset_completed.loc[dataset_completed["branch"] == constants.SINGAPORE_BRANCH]
    frequencies.generate_wordcloud(singapore_df, TOP_N, constants.SINGAPORE_FILE)

    singapore_pos_df = positive_df.loc[positive_df["branch"] == constants.SINGAPORE_BRANCH]
    frequencies.generate_wordcloud(singapore_pos_df, TOP_N, constants.SINGAPORE_POS_FILE)

    singapore_neg_df = negative_df.loc[negative_df["branch"] == constants.SINGAPORE_BRANCH]
    frequencies.generate_wordcloud(singapore_neg_df, TOP_N, constants.SINGAPORE_NEG_FILE)
