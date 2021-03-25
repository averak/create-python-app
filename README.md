# create python app

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

CLI tool to quickstart Python app.

## Requirement

- Python3

## Installation

```sh
$ git clone <this repo>
$ cd <this repo>

$ pip install wheel
$ python setup.py sdist bdist_wheel
$ pip install -e .
```

## Usage

```sh
$ create-python-app
app name : <app name>
author : <author name>
description : <app description>
app version : <app version>
python version : <python version>
Created <app name> app.
```

### Created Project

```
<app name>
├── .gitignore
├── LICENSE
├── Pipfile
├── README.md
├── core
│   └── __init__.py
├── main.py
├── setup.py
└── tests
    └── .keep
```
