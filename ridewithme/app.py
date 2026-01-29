from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
"""
ridewithme/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│
│   ├── blueprints/
│   │   ├── rides/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   ├── services.py
│   │   │   └── repository.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── home.html
│
│   └── static/
│
├── migrations/
├── run.py
└── requirements.txt
"""