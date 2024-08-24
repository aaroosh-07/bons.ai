# bons.ai

bons.ai is web application, which allows you to perform Question Answering task on pdf files uploaded or text provided. Currently we have developed a simple python script to use hugging face models to perform question answering task.

## Setup

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

1. Activate the virtual environment

```
//for windows
virtualenv/Scripts/Activate.ps1 //In Powershell

//for linux/ Mac
source virtualenv/bin/activate
```

2. Run the following commad

```
python main.py
```
