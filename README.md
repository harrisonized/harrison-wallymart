

## Introduction

Object oriented back-end will be contained in `wallymart`, everything front-end will be contained in `wallymart_django`.



## Project X Prompt

For those students who have no ideas or just want something to work on, you may choose this idea without my permission.

Wallymart has asked you to take on AmazingCo in the online e-commerce space. Wallymart can't seem to catch up, but they have identified several areas that are crucial to a successful e-commerce site:
• high quality customer reviews
• large selection of products
• fast delivery

You know Wallymart does really well in physical in-store space. You also know Wallymart has appetite to radically change the way their e-commerce store is designed today.
You are in the driver seat.

Option #1: Design a web store complete with products, reviews, ordering capabilities, and delivery. You will own this end to end meaning that Wallymart has decided to even own the delivery of the products and not outsource to USPS, UPS, etc.



## Installation

Default conda environment is `django-wallymart`

```django
# create
conda create --name wallymart python=3.8  # The Python version is important!
conda activate wallymart
conda install conda
conda install -c anaconda django
conda install pandas
python setup.py develop
```



## Getting Started

Run `python manage.py runserver` to start the server on http://127.0.0.1:8000/

Currently available pages:

1. http://127.0.0.1:8000/
2. http://127.0.0.1:8000/store/
3. http://127.0.0.1:8000/admin/



## Project Directory Structure

```
harrison-wallymart/
├── ref/
│   └── notes.txt
├── wallymart/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── apps
│       └── store
│           ├── migrations/
│           │   └── __init__.py
│           ├── __init__.py
│           ├── admin.py
│           ├── apps.py
│           ├── models.py
│           ├── tests.py
│           ├── urls.py
│           └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── setup.py
└── README.md
```

