FROM python:3.8-slim

RUN mkdir /app

COPY ./ /app

RUN pip install -r /app/requirements.txt --no-cache-dir

WORKDIR /app
CMD ["python", "main.py", "runserver"]