<style>

    h1 {
        color: #8BE9FD; /* Cyan */
    }

    h2 {
        color: #FF79C6; /* Pink */

    }

    h3, h4 {
        color: #50FA7B; /* Green */
    }

 
</style>

# MySQL-CRUD-with-Django-Tutorial

## Step 0 : Make Development Environment
* Install python : https://www.python.org/downloads/
* Install  package management tool : ( on root path )
```bash
    * pip install pipenv
```
## Step 1 : Navigate to the project directory
```bash
cd CRUD_Tutorial
```
## Step 2 : Create a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
```

## Step 3 : Activate the virtual environment:
```bash
venv\Scripts\activate
```

## Step 4 : Install Django and MySQL Client
```bash
pip install Django mysqlclient
```
## Step 5 : Create a new Django project
```bash
django-admin startproject CRUD_Tutorial
```

## Step 6 : Configure Database Settings
Open the <b>settings.py</b> file within your Django project folder and locate the <b>DATABASES</b> setting. Update the configuration to use MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourdatabase',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Step 7 : Create Database Tables
```bash
python manage.py migrate
```
## Step 8 : Create a Django app
```bash
python manage.py startapp MyApp
```

## Step 9 : include the app in our project
```python
INSTALLED_APPS = [
    "MyApp.apps.MyAppConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```
Now Django knows to include the MyApp app.

## Step 10 : define your model 

## Step 11 : Activating models:
* By running <b>makemigrations</b>, you’re telling Django that you’ve made some changes to your models.

    *   ```bash
        py manage.py makemigrations MyApp
        ```

* The <b>sqlmigrate</b> command in Django is used to display the SQL statements that would be executed for a particular migration.

    *   ```bash
        python manage.py migrate
        ```

## Step 12 : Admin Panel (Optional):
If you want to manage your <b>Student</b> model through the Django admin panel, you can register it. Open the <b>admin.py</b> file in your app directory and add the following:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

## Step 13: Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
## Step 14: Run the Development Server
```bash
python manage.py runserver
```

<br><br>

# Django serializers step by step.

## Step 1: Install Django REST Framework
```bash
pip install djangorestframework
```

## Step 2: Create a Django Model

```python
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name    
```
## Step 3: Create a Serializer
```python
# serializers.py
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```
## Step 4: Use the Serializer in Views 
```python
# views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        # Read (List) operation
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create operation
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRetrieveUpdateDeleteView(APIView):
    def get_object(self, pk):
        # Helper function to get a student object by ID
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk, *args, **kwargs):
        # Read (Retrieve) operation
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        # Update operation
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        # Delete operation
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
## Step 5: Configure URLs

###  yourapp/urls.py
```python
# appurls.py
from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDeleteView

urlpatterns = [
    # URL patterns for the CRUD views
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteView.as_view(), name='student-retrieve-update-delete'),
]

```
### yourproject/urls.py

```python
# yourproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your app's URLs
    path('api/', include('yourapp.urls')),  # Replace 'yourapp' with your app's name
]
```


