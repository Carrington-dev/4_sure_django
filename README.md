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

```Docker

docker-compose up -d --build

```
