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




ADD . /staff_profiles/

CMD gunicorn -b :$PORT staff_profiles.wsgi