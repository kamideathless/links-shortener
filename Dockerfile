FROM python:3.12-slim
WORKDIR /links-shorter
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /links-shorter

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . .
EXPOSE 8000
RUN chmod a+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]