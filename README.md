# PurrStream Backend

## Prerequisites

- Python 3.7
- pip3
- pipenv (`pip install pipenv`)
- sqlite3

## Installation

In root directory:

```bash
pipenv install
```

## Run Server

In root directory:

```bash
pipenv shell
python manage.py migrate
python manage.py runserver
```

To access the server in the CodeAnywhere container with the preview link, it needs to run at `0.0.0.0:3000`

```bash
python manage.py runserver 0.0.0.0:3000
```

## Create Admin user

```bash
python manage.py createsuperuser
```
