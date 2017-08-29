# API Star - Talk

[![license][license-image]][license-url]

This is a simple CRUD app written with [API Star](https://github.com/encode/apistar).

## Pre Requirements

  1. [Python3](https://python.org).
  2. [MongoDB](https://www.mongodb.com/).

## Installation

  1. Run MongoDB `mongod`
  2. Install requirements with `pip3 install -r requirements.txt`
  3. Run API Star `apistar run`
  4. Hit the API at [http://localhost:8080](http://localhost:8080)

## API

To look at and play with the API you can go to [http://localhost:8080/docs](http://localhost:8080/docs)

## Tests

Run the tests by execute `apistar test`

## Run for production

Use `uvicorn` to run the app, and change `--workers` flag to how many CPU cores you have on the server

```
$ uvicorn app:app --workers=4 --bind=0.0.0.0:5000 --pid=pid
```
