Django app. This is extra if I finish the command-line version early.



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

