FROM python:3.10-slim


WORKDIR /docusketch


ADD ./ /docusketch/

COPY ./requirements.txt /docusketch/

RUN apt-get update \
    && apt-get -y install libpq-dev python-dev-is-python3 gcc


RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8080


CMD python -m app.main