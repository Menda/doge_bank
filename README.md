# doge_bank

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
