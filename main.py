from fastapi import FastAPI, Path
from controllers import reviews
from init_dataset import positive_frequencies, dataset_completed
from models.reviews import FrequentTermsList, FrequentTerms, ReviewsCount
from fastapi.middleware.cors import CORSMiddleware
from routers import branches, ratings, by_year, time_series
import time_series_init

app = FastAPI()
app.include_router(branches.router, tags=["By branches"])
app.include_router(ratings.router, tags=["By ratings"])
app.include_router(by_year.router, tags=["By year"])
app.include_router(time_series.router, tags=["Time series"])

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/topFeatures/{top_n}", response_model=FrequentTermsList, tags=["General reviews"])
async def top_features(top_n: int = Path(None, description="Top N features to be displayed")):
    # TODO: Change the dataset here to one with all the terms frequencies, not only positive ones
    most_frequent = reviews.get_top_n_frequent_terms(positive_frequencies, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(term=term[0], frequency=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@app.get("/reviews/positive/count", response_model=ReviewsCount, tags=["General reviews"])
async def count_positive_reviews():
    count = reviews.get_positive_reviews_count(dataset_completed)
    return ReviewsCount(count=count)


@app.get("/reviews/negative/count", response_model=ReviewsCount, tags=["General reviews"])
async def count_negative_reviews():
    count = reviews.get_negative_reviews_count(dataset_completed)
    return ReviewsCount(count=count)
