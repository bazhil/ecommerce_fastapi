# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /ecommerce_fastapi
COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade Pillow

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]