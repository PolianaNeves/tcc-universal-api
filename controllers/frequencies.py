import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from wordcloud import WordCloud
import os


def get_terms_frequencies(dataset, top_n):
    stop_words = ["universal", "studios", "park", "day", "year", "month", "disney"]

    vectorizer_train = TfidfVectorizer(ngram_range=(1, 1), strip_accents='ascii', stop_words=stop_words)
    train_vectors = vectorizer_train.fit_transform(dataset["tokens"])

    indices = np.argsort(vectorizer_train.idf_)[::-1]
    features = vectorizer_train.get_feature_names_out()
    top_n = top_n
    top_features = [features[i] for i in indices[-top_n:]]
    top_idf = [vectorizer_train.idf_[i] for i in indices[-top_n:]]
    top_idf.sort(reverse=False)

    frequencies_and_terms = zip(top_features, top_idf)
    frequencies_dict = dict(frequencies_and_terms)

    return frequencies_dict


def generate_wordcloud(dataset, top_n, file_name):
    frequencies_dict = get_terms_frequencies(dataset, top_n)
    wc = WordCloud(background_color="black", width=1000, height=1000).generate_from_frequencies(frequencies_dict)
    wc.to_file(os.path.join("./assets/wordcloud", file_name))


def generate_df_from_frequencies_dict(frequencies_dict):
    return pd.DataFrame.from_dict([frequencies_dict]).T.rename(columns={0: 'frequency'}, inplace=False)


def get_top_n_frequent_terms(dataset, top_n):
    frequent_terms = get_terms_frequencies(dataset, top_n)
    temp_dataset = generate_df_from_frequencies_dict(frequent_terms)
    sorted_dataset = temp_dataset.sort_values(by="frequency", ascending=False)
    sorted_dataset = sorted_dataset.reset_index()
    sorted_dataset.columns = ["term", "frequency"]
    return np.array(sorted_dataset.head(top_n))
