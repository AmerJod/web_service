FROM python:3.7.4

WORKDIR /usr/src/service

COPY . .

ENV FLASK_ENV="production"

# database credentials
ENV POSTGRES_USER="amer"
ENV POSTGRES_PASSWORD="pwd123456"
ENV POSTGRES_DB="db_postgres"

# install the requirements
RUN pip install -r requirements.txt

# install the webserver app
RUN pip install .

## install the common lib
#WORKDIR /usr/src/service/common
#COPY . ./../common
#RUN pip install .

EXPOSE 80/tcp

CMD [ "uwsgi", "app.ini" ]
