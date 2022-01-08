from fastapi import FastAPI, Path
from controllers import labeled_reviews
from init_dataset import positive_frequencies, dataset_completed
from models.responses.labeled_reviews import FrequentTermsList, FrequentTerms, ReviewsCount, \
    ReviewsCountByYearList, ReviewsCountByYear, ReviewsCountByBranchList, ReviewsCountByBranch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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


@app.get("/topFeatures/{top_n}", response_model=FrequentTermsList)
async def top_features(top_n: int = Path(None, description="Top N features to be displayed")):
    # TODO: Change the dataset here to one with all the terms frequencies, not only positive ones
    most_frequent = labeled_reviews.get_top_n_frequent_terms(positive_frequencies, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(term=term[0], frequency=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@app.get("/reviews/count/by/year", response_model=ReviewsCountByYearList)
async def count_positive_reviews_by_year():
    reviews_by_year = labeled_reviews.get_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearList(data=reviews_by_year)


@app.get("/reviews/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_positive_reviews_by_year(year: int = Path(None, description="Year to applied to the filter")):
    count_by_year = labeled_reviews.get_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))


@app.get("/reviews/count/by/branch", response_model=ReviewsCountByBranchList)
async def count_reviews_by_branch():
    by_branch = labeled_reviews.get_reviews_count_by_branch(dataset_completed)
    return ReviewsCountByBranchList(data=by_branch)


@app.get("/reviews/count/by/branch/{branch}", response_model=ReviewsCountByBranch)
async def count_reviews_by_branch(branch: str = Path(None, description="Branch to filter reviews")):
    count_by_branch = labeled_reviews.get_reviews_count_filter_by_branch(dataset_completed, branch)
    return ReviewsCountByBranch(branch=branch, count=count_by_branch)


@app.get("/reviews/positive/count", response_model=ReviewsCount)
async def count_positive_reviews():
    count = labeled_reviews.get_positive_reviews_count(dataset_completed)
    return ReviewsCount(count=count)


@app.get("/reviews/positive/count/by/year", response_model=ReviewsCountByYearList)
async def count_positive_reviews_by_year():
    reviews_by_year = labeled_reviews.get_positive_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearList(data=reviews_by_year)


@app.get("/reviews/positive/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_positive_reviews_by_year(year: int = Path(None, description="Year to applied to the filter")):
    count_by_year = labeled_reviews.get_positive_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))


@app.get("/reviews/positive/count/by/branch", response_model=ReviewsCountByBranchList)
async def count_positive_reviews_by_branch():
    reviews_by_year = labeled_reviews.get_positive_reviews_count_by_branch(dataset_completed)
    return ReviewsCountByBranchList(data=reviews_by_year)


@app.get("/reviews/positive/count/by/branch/{branch}", response_model=ReviewsCountByBranch)
async def count_positive_reviews_by_branch(branch: str = Path(None, description="Branch to filter reviews")):
    count_by_branch = labeled_reviews.get_positive_reviews_count_filter_by_branch(dataset_completed, branch)
    return ReviewsCountByBranch(branch=branch, count=count_by_branch)


@app.get("/reviews/negative/count", response_model=ReviewsCount)
async def count_negative_reviews():
    count = labeled_reviews.get_negative_reviews_count(dataset_completed)
    return ReviewsCount(count=count)


@app.get("/reviews/negative/count/by/year", response_model=ReviewsCountByYearList)
async def count_negative_reviews_by_year():
    reviews_by_year = labeled_reviews.get_negative_reviews_count_by_year(dataset_completed)
    return ReviewsCountByYearList(data=reviews_by_year)


@app.get("/reviews/negative/count/by/year/{year}", response_model=ReviewsCountByYear)
async def count_negative_reviews_by_year(year: int = Path(None, description="Year to applied to the filter")):
    count_by_year = labeled_reviews.get_negative_reviews_count_filter_by_year(dataset_completed, year)
    return ReviewsCountByYear(count=count_by_year, year=str(year))


@app.get("/reviews/negative/count/by/branch", response_model=ReviewsCountByBranchList)
async def count_negative_reviews_by_branch():
    reviews_by_branch = labeled_reviews.get_negative_reviews_count_by_branch(dataset_completed)
    return ReviewsCountByBranchList(data=reviews_by_branch)


@app.get("/reviews/negative/count/by/branch/{branch}", response_model=ReviewsCountByBranch)
async def count_negative_reviews_by_branch(branch: str = Path(None, description="Branch to filter the reviews")):
    count_by_branch = labeled_reviews.get_negative_reviews_count_filter_by_branch(dataset_completed, branch)
    return ReviewsCountByBranch(count=count_by_branch, branch=branch)
