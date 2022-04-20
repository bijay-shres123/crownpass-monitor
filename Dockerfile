FROM python:3.8-alpine
LABEL maintainer="admin@crownpass.com"

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

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