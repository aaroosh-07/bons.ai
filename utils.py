from enum import Enum
import httpx

class ModelName(str, Enum):
    distilbert = "distilbert-base-cased"
    roberta = "roberta-base-squad2"
    google = "google-bert"
    electra_large_discriminator = "electra_large_discriminator"

API_URL = {
    'distilbert-base-cased' : "https://api-inference.huggingface.co/models/distilbert/distilbert-base-cased-distilled-squad",
    'roberta-base-squad2' : "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2",
    'google-bert' : "https://api-inference.huggingface.co/models/google-bert/bert-large-uncased-whole-word-masking-finetuned-squad",
    'electra_large_discriminator': "https://api-inference.huggingface.co/models/ahotrod/electra_large_discriminator_squad2_512"
}

def selectModel(model: ModelName)->str:
    return API_URL[model.value]

async def send_rest_api_req(payload: dict, headers: dict, api_url: str)->dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(headers= headers, url = api_url, json= payload)
        data = response.json()
        return data