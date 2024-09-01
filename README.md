# bons.ai

bons.ai is web application, which allows you to perform Question Answering task on pdf files uploaded or text provided. Currently we have developed a simple python script to use hugging face models to perform question answering task.

## Getting Started

### Setting up Environment

1. Create python virtual environment using this command

```
python -m venv virtualenv
```

2. Activate the virtual environment

```
//for windows
virtualenv/Scripts/Activate.ps1 //In Powershell

//for linux/ Mac
source virtualenv/bin/activate
```

3. Install all the required modules.

```
pip install -r requirements.txt
```

### Adding API_TOKEN from hugging face

1. generate your API_TOKEN from hugging face.
2. create a `.env` file in root directory of your project.
3. add the following content in your `.env` file

```
API_TOKEN = "<your api token>"
```

### Running the script

Run the following commad after activating the virtual environment.

```
cd experiments
python main.py
```

### Running FastAPI server

This command will run fastapi development server on localhost:8000

```
fastapi dev server.py
```

## API Endpoints

The following API endpoints have been implmented.

### Request

`GET /`

```
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json'
```

### Response body

```
{
  "Message": "welcome to bons.ai"
}
```

### Request

`POST /prompt`

```
curl -X 'POST' \
  'http://127.0.0.1:8000/prompt' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "what is my name",
  "context": "my name is aaroosh",
  "model": "distilbert-base-cased"
}'
```

In this POST request we need to send request body having the following structure

```
{
  "question": string,
  "context": string,
  "model": "distilbert-base-cased" or "roberta-base-squad2" or "google-bert" or "electra_large_discriminator"
}
```

### Response body

```
{
  "score": 0.9413116574287415,
  "start": 11,
  "end": 18,
  "answer": "aaroosh"
}
```
