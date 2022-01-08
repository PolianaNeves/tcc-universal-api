from fastapi import FastAPI, Path
from controllers import labeled_reviews
from init_dataset import positive_frequencies, dataset_completed
from models.responses.labeled_reviews import FrequentTermsListResponse, FrequentTermsResponse, ReviewsCount, \
    ReviewsCountByYearResponse, ReviewsCountByYear
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/topFeatures/{top_n}", response_model=FrequentTermsListResponse)
async def top_features(top_n: int = Path(None, description="Top N features to be displayed")):
    # TODO: Change the dataset here to one with all the terms frequencies, not only positive ones
    most_frequent = labeled_reviews.get_top_n_frequent_terms(positive_frequencies, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTermsResponse(term=term[0], frequency=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsListResponse(data=frequent_terms)


@app.get("/reviews/positive/count", response_model=ReviewsCount)
async def count_positive_reviews():
    count = labeled_reviews.get_positive_reviews_count(dataset_completed)
    return ReviewsCount(count=count)


@app.get("/reviews/negative/count", response_model=ReviewsCount)
async def count_negative_reviews():
    count = labeled_reviews.get_negative_reviews_count(dataset_completed)
    return ReviewsCount(count=count)


@app.get("/reviews/count/by/year", response_model=ReviewsCountByYearResponse)
async def count_positive_reviews_by_year():
    reviews_by_year = labeled_reviews.get_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearResponse(data=reviews_by_year)


@app.get("/reviews/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_positive_reviews_by_year(year: int = Path(None, description="Year to applied to the filter")):
    count_by_year = labeled_reviews.get_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))


@app.get("/reviews/positive/count/by/year", response_model=ReviewsCountByYearResponse)
async def count_positive_reviews_by_year():
    reviews_by_year = labeled_reviews.get_positive_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearResponse(data=reviews_by_year)


@app.get("/reviews/positive/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_positive_reviews_by_year(year: int = Path(None, description="Year to applied to the filter")):
    count_by_year = labeled_reviews.get_positive_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))


@app.get("/reviews/negative/count/by/year", response_model=ReviewsCountByYearResponse)
async def count_negative_reviews_by_year():
    reviews_by_year = labeled_reviews.get_negative_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearResponse(data=reviews_by_year)


@app.get("/reviews/negative/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_negative_reviews_by_year(year: int = Path(None, description="Year to applied to the filter")):
    count_by_year = labeled_reviews.get_negative_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))

