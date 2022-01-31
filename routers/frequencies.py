from fastapi import APIRouter, Path, Response, status
from inits.init_dataset import dataset_completed
from controllers import frequencies
from models.frequencies import FrequentTerms, FrequentTermsList
from constants import POSITIVE, NEGATIVE
import base64
from models.images import ImageDecodedResponse
import os

router = APIRouter()


@router.get("/reviews/top/{top_n}/all/terms", response_model=FrequentTermsList)
async def top_terms(top_n: int = Path(None, description="Top N features to be displayed")):
    most_frequent = frequencies.get_top_n_frequent_terms(dataset_completed, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(label=term[0], value=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@router.get("/reviews/top/{top_n}/positive/terms", response_model=FrequentTermsList)
async def top_positive_terms(top_n: int = Path(None, description="Top N features to be displayed")):
    positive_dataset = dataset_completed.loc[dataset_completed["label"] == POSITIVE]
    most_frequent = frequencies.get_top_n_frequent_terms(positive_dataset, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(label=term[0], value=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@router.get("/reviews/top/{top_n}/negative/terms", response_model=FrequentTermsList)
async def top_positive_terms(top_n: int = Path(None, description="Top N features to be displayed")):
    negative_dataset = dataset_completed.loc[dataset_completed["label"] == NEGATIVE]
    most_frequent = frequencies.get_top_n_frequent_terms(negative_dataset, top_n)
    frequent_terms = []
    for term in most_frequent:
        frequent_term = FrequentTerms(label=term[0], value=term[1])
        frequent_terms.append(frequent_term)

    return FrequentTermsList(data=frequent_terms)


@router.get("/reviews/wordcloud/{name}/top/terms", response_model=ImageDecodedResponse)
async def top_terms_wordcloud(response: Response,
                              name: str = Path(None, description="Wordcloud name to be returned")):
    filename = f"{name}.jpeg"
    path = os.path.join("./assets/wordcloud", filename)
    if os.path.exists(path):
        b64_string = base64.b64encode(open(path, "rb").read())
        return ImageDecodedResponse(data=b64_string.decode('utf-8'))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
