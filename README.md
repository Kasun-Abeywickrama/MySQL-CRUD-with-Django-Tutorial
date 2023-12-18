# MySQL-CRUD-with-Django-Tutorial

## Step 0 : Make Development Environment
* Install python : https://www.python.org/downloads/
* Install  package management tool : ( on root path )
    * pip install pipenv

## Step 1 : Navigate to the project directory
cd MyApp

## Step 2 : Create a Virtual Environment with Pipenv and install django inside that environment.
pipenv install django

## Step 3 : Activate the Virtual Environment with Pipenv
pipenv shell


## Step 4 : Install Django and MySQL Client
pip install Django mysqlclient

## Step 5 : Create a new Django project
django-admin startproject CRUD_Tutorial .

## Step 6 : Configure Database Settings
Open the <b>settings.py</b> file within your Django project folder and locate the <b>DATABASES</b> setting. Update the configuration to use MySQL:

DATABASES = {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;'default': {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'ENGINE': 'django.db.backends.mysql',<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'NAME': 'yourdatabase',<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'USER': 'yourusername',<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'PASSWORD': 'yourpassword',<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'HOST': 'localhost',<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'PORT': '3306',<br>
    &nbsp;&nbsp;&nbsp;&nbsp;}<br>
}

## Step 7 : Create Database Tables
python manage.py migrate

## Step 8 : Create a Django app
python manage.py startapp MyApp

## Step 9 : include the app in our project
INSTALLED_APPS = [<br>
    <b>"MyApp.apps.MyAppConfig",</b><br>
    "django.contrib.admin",<br>
    "django.contrib.auth",<br>
    "django.contrib.contenttypes",<br>
    "django.contrib.sessions",<br>
    "django.contrib.messages",<br>
    "django.contrib.staticfiles",<br>
]

Now Django knows to include the MyApp app.

## Step 10 : define your model 

## Step 11 : Activating models:
* By running <b>makemigrations</b>, you’re telling Django that you’ve made some changes to your models.

    * py manage.py makemigrations MyApp


* The <b>sqlmigrate</b> command in Django is used to display the SQL statements that would be executed for a particular migration.

    * python manage.py migrate

## Step 12 : Admin Panel (Optional):
If you want to manage your <b>Student</b> model through the Django admin panel, you can register it. Open the <b>admin.py</b> file in your app directory and add the following:

from django.contrib import admin<br>
from .models import Student

admin.site.register(Student)


## Step 13: Create a Superuser (Optional)
python manage.py createsuperuser

## Step 14: Run the Development Server
python manage.py runserver





