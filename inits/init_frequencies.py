from controllers import frequencies, POSITIVE, NEGATIVE
from init_dataset import dataset_completed

TOP_N = 100

if len(os.listdir('./assets/wordcloud')) == 1:
    frequencies.generate_wordcloud(dataset_completed, TOP_N, "default_wordcloud.png")

    positive_df = dataset_completed.loc[dataset_completed["label"] == POSITIVE]
    frequencies.generate_wordcloud(positive_df, TOP_N, "default_wordcloud.png")

    negative_df = dataset_completed.loc[dataset_completed["label"] == NEGATIVE]
    frequencies.generate_wordcloud(negative_df, TOP_N, "default_wordcloud.png")
