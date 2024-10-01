FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server.py /code/server.py
COPY ./utils.py /code/utils.py
COPY ./config.py /code/config.py

EXPOSE 8080

CMD ["fastapi", "run", "server.py", "--port", "8080"]