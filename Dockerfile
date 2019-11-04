FROM python:3.7.4

WORKDIR /usr/src/service

COPY service .

ENV FLASK_ENV="production"

# Database credentials
ENV POSTGRES_USER="postgres"
ENV POSTGRES_PASSWORD="postgres"
ENV POSTGRES_DB="postgres"


# install the requirements
RUN pip install -r requirements.txt

# install the webserver app
RUN pip install .


COPY common .
# install the common lib
RUN pip install .


EXPOSE 80/tcp

CMD [ "uwsgi", "app.ini" ]

