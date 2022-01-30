import inits
from fastapi import FastAPI, Path
from controllers import reviews
from inits.init_dataset import dataset_completed
from models.reviews import ReviewsCount
from fastapi.middleware.cors import CORSMiddleware
from routers import branches, ratings, by_year, time_series, frequencies, attractions


app = FastAPI()
app.include_router(branches.router, tags=["By branches"])
app.include_router(ratings.router, tags=["By ratings"])
app.include_router(by_year.router, tags=["By year"])
app.include_router(time_series.router, tags=["Time series"])
app.include_router(frequencies.router, tags=["Frequencies"])
app.include_router(attractions.router, tags=["Attractions"])

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


@app.get("/reviews/positive/count", response_model=ReviewsCount, tags=["General reviews"])
async def count_positive_reviews():
    count = reviews.get_positive_reviews_count(dataset_completed)
    return ReviewsCount(value=count)
    


@app.get("/reviews/negative/count", response_model=ReviewsCount, tags=["General reviews"])
async def count_negative_reviews():
    count = reviews.get_negative_reviews_count(dataset_completed)
    return ReviewsCount(value=count)
