FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY poetry.lock pyproject.toml /code/
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

COPY . /code/
