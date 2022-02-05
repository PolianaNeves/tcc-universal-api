from models.reviews import ReviewsCountBy, ReviewsGroup
from models.attractions import ReviewsCountByAttraction
from inits.init_dataset import dataset_attractions_count
import pandas as pd
from autots import AutoTS
import matplotlib.pyplot as plt
from prophet import Prophet
import os
import constants

my_path = os.path.relpath(os.path.join(os.path.dirname(__file__), os.pardir))
branches = [constants.FLORIDA_BRANCH, constants.JAPAN_BRANCH, constants.SINGAPORE_BRANCH]

def count_reviews_by(dataset, column_filter):
    grouped_df = dataset.groupby([column_filter])
    reviews_group_list = []
    df_pos = dataset[dataset["label"] == constants.POSITIVE]
    df_neg = dataset[dataset["label"] == constants.NEGATIVE]
    default = ReviewsCountBy(label=constants.DEFAULT_BRANCH, total=len(dataset), positive=len(df_pos), negative=len(df_neg))
    reviews_group_list.append(ReviewsGroup(key=constants.DEFAULT_BRANCH, data=[default]))
    for key, item in grouped_df:
        reviews_count_by = []
        df_full_pos = item[item["label"] == constants.POSITIVE]
        df_full_neg = item[item["label"] == constants.NEGATIVE]
        default = ReviewsCountBy(label=constants.DEFAULT_BRANCH, total=len(item), positive=len(df_full_pos), negative=len(df_full_neg))
        reviews_count_by.append(default)
        for branch in branches:
            df_branch = item[item["branch"] == branch]
            df_branch_pos = df_branch[df_branch["label"] == constants.POSITIVE]
            df_branch_neg = df_branch[df_branch["label"] == constants.NEGATIVE]
            branch_by = ReviewsCountBy(label=branch, total=len(df_branch), positive=len(df_branch_pos), negative=len(df_branch_neg))
            reviews_count_by.append(branch_by)
        reviews_group_list.append(ReviewsGroup(key=str(key), data=reviews_count_by))
    return reviews_group_list


def count_reviews_by_attraction(column_filter):
    list_by_attraction = []
    name = f'{column_filter}_name'
    temp_df = dataset_attractions_count[[name, column_filter]]
    for index, row in temp_df.iterrows():
        if float(row[column_filter]) > 0:
            attraction_count = ReviewsCountByAttraction(label=row[name], value=row[column_filter])
            list_by_attraction.append(attraction_count)
    return list_by_attraction


def parse_df(dataset):
    """Parse the dataset to the expected output to autoTs models"""
    grouped_ds = dataset.groupby(["year", "month"])
    parsed_df = pd.DataFrame(columns=["date", "reviews_count"])
    for key, item in grouped_ds:
        parsed_df = parsed_df.append({"date": f'{key[0]}-{key[1]}', "reviews_count": len(item)}, ignore_index=True)
    parsed_df['date'] = pd.to_datetime(parsed_df['date'], infer_datetime_format=True, format='%y%m')
    parsed_df['reviews_count'] = pd.to_numeric(parsed_df["reviews_count"])
    parsed_df = parsed_df[["date", "reviews_count"]]
    parsed_df["date"] = pd.to_datetime(parsed_df.date)
    return parsed_df


def get_indexed_dataframe(df):
    return df.set_index('date')


def train_and_predict(df):
    model = AutoTS(forecast_length=30, frequency='infer',
                   ensemble='simple', drop_data_older_than_periods=100)
    model = model.fit(df, date_col='date', value_col='reviews_count', id_col=None)
    prediction = model.predict()
    forecast = prediction.forecast
    return forecast


def plot_prediction(df, file_name, fig_number):
    forecast = train_and_predict(df)
    temp_df = get_indexed_dataframe(df)
    plt.figure(fig_number)
    temp_df['reviews_count'].plot(figsize=(12, 8), title='Reviews Count Over the Years', fontsize=20, label='Train')
    forecast['reviews_count'].plot(figsize=(12, 8), title='Reviews Count Over the Years', fontsize=20, label='Test')
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join("./assets", file_name), dpi=72)


def get_limit_index(dataset):
    """Get the limit index for train and model of the dataset. Considering 75%"""
    return int(0.75 * len(dataset))


def train_with_prophet_model(dataset):
    """Train the data with Prophet model"""
    dataset.columns = ["ds", "y"]
    prophet = Prophet(weekly_seasonality=True)
    limit_index = get_limit_index(dataset)
    train = dataset[:limit_index]
    test = dataset[limit_index:]
    prophet.fit(train)
    return prophet


def predict_with_prophet_model(prophet, file_name):
    """Make a prediction with prophet model and periods (param)."""
    future = prophet.make_future_dataframe(periods=2555)
    forecast = prophet.predict(future)
    figure = prophet.plot_components(forecast)
    figure.savefig(os.path.join("./assets/details", file_name), dpi=72)
