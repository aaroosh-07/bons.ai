import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

API_URL = {
    'distilbert-base-cased' : "https://api-inference.huggingface.co/models/distilbert/distilbert-base-cased-distilled-squad",
    'roberta-base-squad2' : "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2",
    'google-bert' : "https://api-inference.huggingface.co/models/google-bert/bert-large-uncased-whole-word-masking-finetuned-squad",
    'electra_large_discriminator': "https://api-inference.huggingface.co/models/ahotrod/electra_large_discriminator_squad2_512"
}

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload, api_url):
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

def select_model():
    modelChoice = int(input("""Enter which model to choose:
                            1. distilbert-base-cased
                            2. roberta-base-squad2
                            3. google-bert
                            4. electra_large_discriminator
                            """))
    model = str()
    if modelChoice == 1:
        model = "distilbert-base-cased"
    elif modelChoice == 2:
        model = "roberta-base-squad2"
    elif modelChoice == 3:
        model = "google-bert"
    elif modelChoice == 4:
        model = "electra_large_discriminator"
    else:
        print("using distilbert base cased as default model")
        model = "distilbert-base-cased"
    
    return model

def start():
    model = select_model()
    context = input("Enter the context: ")
    question = input("Enter the question: ")
    data = query(
        {
            "inputs": {
                "question": f"{question}",
                "context": f"{context}",
            }
        },
        API_URL[model]
    )

    print(data)

start()