FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install

EXPOSE 5000

CMD ["pipenv", "run", "gunicorn", "--config", "gunicorn_config.py", "app:app"]
