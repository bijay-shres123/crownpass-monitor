#!/usr/bin/env bash
FROM python:3.8-alpine

LABEL maintainer="admin@crownpass.com"



COPY ./requirements.txt /requirements.txt
COPY ./staff_profiles /staff_profiles

WORKDIR /staff_profiles

# Providing docker write access
# RUN chown -R staff_profiles:staff_profiles /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django-user



ENV PATH="/py/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
ENV DEBUG=True


ADD . /staff_profiles/

CMD python manage.py runserver 0.0.0.0:8000
# CMD gunicorn -b :$PORT staff_profiles.wsgi