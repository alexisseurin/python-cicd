# python-cicd

## Create a virtual environment
```bash
python -m venv python-env

# Activate virtual environment (Linux/Mac)
source python-env/bin/activate

# Activate virtual environment (Windows)
python-env\Scripts\activate
```

## Set up the backend by installing required packages
```bash
pip install -r requirements.txt
```

##  Create a Django project
```bash
django-admin startproject myproject
```

## Create a Django app
```bash
cd myproject
python manage.py startapp myapp
```

## Add the app to the project
```bash
INSTALLED_APPS = [
    # Add this line in your settings.py file inside myproject folder
    'myapp',
    # ...
]
```

# Run the development server
```bash
python manage.py runserver
```

# Test
```bash
http://127.0.0.1:8000/hello/
```

# Run Tests
```bash
python manage.py test
```