from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from config import settings
from utils import ModelName, selectModel, send_rest_api_req

class Prompt(BaseModel):
    question: str
    context: str
    model: ModelName = ModelName.distilbert

app = FastAPI()

@app.get("/")
def home_route():
    return {"Message": "welcome to bons.ai"}

@app.post("/prompt")
async def prompt_llm(prompt: Prompt, response: Response):
    context = prompt.context
    question = prompt.question
    headers = {"Authorization": f"Bearer {settings.api_token}"}
    payload = {
            "inputs": {
                "question": f"{question}",
                "context": f"{context}",
            }
        }
    api_url = selectModel(prompt.model)
    data = await send_rest_api_req(payload= payload, headers= headers, api_url= api_url)
    if data.status_code == 503:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return data.content