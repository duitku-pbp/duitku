# Setting Up

Clone the repository

```
git clone git@github.com:duitku-pbp/duitku.git
cd duitku
```

Create a virtual environment with

```
Create Virtual Environment:
python3 -m venv env

Ubuntu/MacOS:
source /env/bin/activate
pip install -r requirements.txt

Windows:
env\Scripts\activate.bat
pip install -r requirements.txt
```

Migrate all the initial migrations

```
python manage.py migrate
```

Start Your App/Module

```
python manage.py startapp [APP_NAME]
Example: python manage.py startapp kalkulator
```

Start Development

```
python manage.py runserver
```
