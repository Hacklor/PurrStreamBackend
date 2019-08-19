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

## Create Admin user

```bash
python manage.py createsuperuser
```
