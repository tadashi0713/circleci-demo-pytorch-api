FROM python:3.9

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "python", "app.py"]

EXPOSE 5000
