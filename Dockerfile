FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWEITEBYTECODE=1

WORKDIR /app

COPY pyproject.toml /app

RUN pip install "poetry==1.7.0"
RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1
RUN poetry install

COPY . /app