FROM python:3.7

# Do not buffer log messages in memory; some messages can be lost otherwise
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD requirements/base.txt requirements/base.txt
ADD requirements/production.txt requirements/production.txt
RUN pip install -r requirements/production.txt

ADD . /code

ENTRYPOINT ["bash", "/code/docker-entrypoint.sh"]
