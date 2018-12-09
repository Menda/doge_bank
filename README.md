# doge_bank

[![Build Status](https://travis-ci.org/Menda/doge_bank.svg?branch=master)](https://travis-ci.org/Menda/doge_bank)

Doge Bank is your Bank of Trust ™.

![Doge Bank logo](https://s3.amazonaws.com/menda/other/doge_bank_logo.png)


## Getting started

You must have [Docker](https://www.docker.com/) installed.

Build the image:

```bash
docker-compose build
```

Run the web server:

```bash
docker-compose up
```

Open your browser with URL `http://localhost:8000`.
For the admin panel `http://localhost:8000/admin`
(user: `admin`, password: `admin`).


That's it!


## Run the tests

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' doge_bank
```


## Clean database

If you would like to clean the database and start the application, do:

```bash
docker-compose up --renew-anon-volumes --force-recreate --build
```

## About

This application is **not production ready**. This means that some changes
need to be done in order to achieve a production-ready status.

Most important changes are detailed in the
[deployment checklist](https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/)
documentation page.

Also, there are some additional improvements which can be done:

* Add to `requirements/production.txt` a production-ready web server like
  [Gunicorn](https://gunicorn.org) or
  [uWSGI](https://uwsgi-docs.readthedocs.io).
* Design a minimal `docker-entrypoint.sh` to just start the web server chosen,
  and let your own deployment orchestrator to do migrations or other stuff.
* Serve static files from a small and fast web server, like
  [NGINX](https://www.nginx.com/). There are several ways to collect static
  files and let NGINX retrieve them, so choose the solution that fits best to
  your architecture.
* Encrypt the IBAN, as it's considered sensitive data.
  [django-fernet-fields](https://django-fernet-fields.readthedocs.io) can help
  for such purpose.
* Add End-to-End tests to check externally from a browser that at least
  the happy path works as intended.
* Add extra template rendering tests to check that we display the relevant
  information that we pass through the context.
