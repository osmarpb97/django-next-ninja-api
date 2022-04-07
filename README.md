## Installation

We need poetry for this, so install poetry first, then

``poetry install``

Apply migrations


```bash
poetry shell
python3 manage.py migrate
```


To start the server 
```bash
python3 manage.py runserver
```