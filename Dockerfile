FROM python:3.8.6-alpine3.12 as pyt

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /fampay
ADD ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . .
RUN python manage.py makemigrations \
    && python manage.py createcachetable \
    && python manage.py migrate \
    && python manage.py crontab add

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]