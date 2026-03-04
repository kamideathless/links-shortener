# Links Shorter

Сервис для сокращения ссылок, FastAIP + PostgreSQL

## Запуск через docker-compose

1. Склонировать репозиторий:

```bash
git clone https://github.com/kamideathless/links-shortener.git
cd links-shorter
```

2. Создать `.env` файл:

```bash
cp .env.example .env
```

3. Запустить:

```bash
docker compose up --build
```

Swagger документация: http://localhost:8000/docs

## Тесты

```bash
poetry run pytest tests/ -v
```

---

> Примечание по тестам: тесты написал самые простенькие — покрывают основную логику без поднятия
> БД. Навыки в тестировании не очень, но всегда готов совершенствоваться в необходимых областях.
