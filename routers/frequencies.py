from fastapi import APIRouter, Path, Response, status
from inits.init_dataset import dataset_completed
from controllers import frequencies
from models.frequencies import FrequentTerms, FrequentTermsList
from fastapi.responses import FileResponse
from constants import POSITIVE, NEGATIVE
import os

router = APIRouter()


@router.get("/reviews/top/{top_n}/all/terms", response_model=FrequentTermsList)
async def top_terms(top_n: int = Path(None, description="Top N features to be displayed")):
    most_frequent = frequencies.get_top_n_frequent_terms(dataset_completed, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(term=term[0], frequency=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@router.get("/reviews/top/{top_n}/positive/terms", response_model=FrequentTermsList)
async def top_positive_terms(top_n: int = Path(None, description="Top N features to be displayed")):
    positive_dataset = dataset_completed.loc[dataset_completed["label"] == POSITIVE]
    most_frequent = frequencies.get_top_n_frequent_terms(positive_dataset, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(term=term[0], frequency=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@router.get("/reviews/top/{top_n}/negative/terms", response_model=FrequentTermsList)
async def top_positive_terms(top_n: int = Path(None, description="Top N features to be displayed")):
    negative_dataset = dataset_completed.loc[dataset_completed["label"] == NEGATIVE]
    most_frequent = frequencies.get_top_n_frequent_terms(negative_dataset, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(term=term[0], frequency=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@router.get("/reviews/wordcloud/{name}/top/terms", response_class=FileResponse)
async def top_terms_wordcloud(response: Response,
                              name: str = Path(None, description="Wordcloud name to be returned")):
    filename = f"{name}.png"
    path = os.path.join("./assets/wordcloud", filename)
    if os.path.exists(path):
        return FileResponse(path)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
