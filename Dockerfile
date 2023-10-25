FROM python:3.11

LABEL maintainer="Marline Khavele<khavelemarline@gmail.com>"

ARG INSTALL_DEV=false

COPY ./pyproject.toml ./poetry.lock* ./Makefile /app/

WORKDIR /app/

RUN apt-get update && apt-get install libpq-dev -y && apt-get clean && poetry config virtualenvs.create false && \
    poetry install $(test "$INSTALL_DEV" = "false" && echo "--no-dev") --no-root --no-interaction --no-ansi

COPY ./src /app/

ENV PYTHONPATH=/app

# Gunicorn will run on port 80. See src/app/config_gunicorn.py
CMD [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "app/config/config_gunicorn.py",  \
    "--log-config", "app/config/logging_container.conf", "--statsd-host", "localhost:8125", "app.main:app"]
