# Clown Management System

## Project Structure

```python

    account/ # application
    client/ # application
    clown/ # application
    troupe/ # application
    expertproj/ # project directory
    manage.py # 

```

## Running the project on your local machine

To run the project

### Step 1 Clone the respository
clone this repository

```bash

git clone git_url
cd git_project/app
```

### Step 2: Install dependencies

```python
python -m venv projectenv
source projectenv/bin/activate # linux
projectenv/Scripts/activate # window remembder use \ instead of / on windows
pip install -r requirements.txt
```

### Step 3

```python

python manage.py runserver 0.0.0.0:8000
```


## Running the project using docker compose

Dockerfile will match the container's port with your port

__build a container and run the application__

```bash
docker-compose up -d --build
```
run commands inside a container
```bash
docker-compose exec web python manage.py createsuperuser
```

## Endpoints

view our endpoints

```
/ # to view all users in the system
/register # to register and view clowns
/clients # to make or create appointments for clients
/login # to login as per FLask given example not a django standard
/clowns # to view clowns
/appointments # to view appointments only
/create_appointments # to create and view appointments
```

### Swagger

swagger is not activated but can easily be activated on just a click to show all endpoints

```bash
pip install django-rest-swagger
```

__settings.py__
```python

INSTALLED_APPS = [
    ...
    'rest_framework_swagger',
    ...
    
]
```
__configure__
```python
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]
```