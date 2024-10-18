# object-detect-api

API for providing descriptions of food images. Developed with Django, Django REST Framework and OpenAI API.

The directory structure of this repository is as follows:

```
object-detect-api/
├── db.sqlite3
├── manage.py
├── object_detector/
│   ├── admin.py
│   ├── apps.py
│   ├── controllers.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── permissions.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __init__.py
│   └── __pycache__/
│       ├── admin.cpython-312.pyc
│       ├── apps.cpython-312.pyc
│       ├── controllers.cpython-312.pyc
│       ├── models.cpython-312.pyc
│       ├── permissions.cpython-312.pyc
│       ├── urls.cpython-312.pyc
│       ├── views.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── object_detect_api/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── __init__.py
│   └── __pycache__/
│       ├── settings.cpython-312.pyc
│       ├── urls.cpython-312.pyc
│       ├── wsgi.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── README.md
├── requirements.txt
├── utils/
│   ├── api_requests/
│   │   ├── object_detection_requests.py
│   │   └── __pycache__/
│   │       └── object_detection_requests.cpython-312.pyc
│   ├── errors/
│   └── helpers/
│       └── object_detection_helpers.py
└── vercel.json
```
