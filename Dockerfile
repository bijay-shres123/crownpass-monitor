FROM python:3.9-alpine
LABEL maintainer="admin@crownpass.com"

COPY ./requirements.txt /requirements.txt
COPY ./staff_profiles /staff_profiles

WORKDIR /staff_profiles

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"


USER django-user

ADD . /staff_profiles/