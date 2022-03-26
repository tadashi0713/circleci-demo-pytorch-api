FROM python:3.8

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "flask", "run"]

EXPOSE 5000
