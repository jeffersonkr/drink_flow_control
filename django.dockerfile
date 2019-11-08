FROM python:3
MAINTAINER Jefferson Kwak <jeffersonkr@hotmail.com>
COPY . /var/www
WORKDIR /var/www/
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD python3 manage.py collectstatic --noinput
CMD python3 manage.py runserver 0.0.0.0:8000