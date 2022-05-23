# PRECLASS SETUP

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django

python -m django --version
django-admin startproject main .

pip install python-decouple
pip freeze > requirements.txt
```
add a gitignore file at same level as env folder

create a new file and name as .env at same level as env folder

copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY

```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

go to settings.py, make amendments below

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

go to terminal

```bash
py manage.py migrate
py manage.py runserver
```

click the link with CTRL key pressed in the terminal and see django rocket.

go to terminal, stop project, add app

```
py manage.py startapp fscohort
```

go to settings.py and add 'fscohort' app to installed apps and add below lines

go to fscohort/models.py

```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

```

go to terminal

```bash
py manage.py makemigrations
py manage.py migrate
python manage.py createsuperuser
```

go to fscohort/admin.py

```python
from django.contrib import admin

from .models import Student
# Register your models here.
admin.site.register(Student)
```

go to Admin site and add student objects

create template folder as fscohort/templates/fscohort

base.html

```html
<!DOCTYPE html>
{% load static %}

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
      integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ"
      crossorigin="anonymous"
    />

    {% comment %}
    <link rel="stylesheet" href=" {% static 'fscohort/css/bootstrap.min.css' %}" />
    {% endcomment %}

    <link rel="stylesheet" href=" {% static 'fscohort/css/style.css' %}  " />

    <title>Document</title>
  </head>

  <body>
    {% comment %} {% include "users/navbar.html" %} {% endcomment %}
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">

      {% block container %}{% endblock container %}
    </div>
    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>
    <script src="{% static 'fscohort/js/timeout.js' %}"></script>
  </body>
</html>
```

index.html

```html
{% extends "fscohort/base.html" %} {% block container %}
<h1>Home Page</h1>

<h3>Student App</h3>

{% endblock container %}
```

go to fscohort/views.py

```python
from django.shortcuts import render

def index(request):
    return render(request, 'fscohort/index.html')

```

go to core/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fscohort.urls')),
]
```

go to fscohort/urls.py

```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='home'),
]
```

run server !


/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - READ(GET)           /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to fscohort/views.py
```python
from .models import Student

def student_list(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'fscohort/student_list.html', context)
```

go to fscohort/urls.py
```python
from django.urls import path
from .views import index, student_list

urlpatterns = [
    path('', index, name='home'),
    path('list/',student_list , name='list'),
]
```

student_list.html
```html
{% extends 'fscohort/base.html' %}

{% block container %}
<ul>
    {% for student in students%}
    <li>{{ student.number }} - {{student.first_name}} {{student.last_name}}</li>
    {%endfor%}
</ul>
{% endblock container %}
```

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - CREATE (POST)       /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to fscohort/forms.py
```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__' 
        labels = {"first_name": "Adınız", "last_name":"Soyadınız", "number":"Numaranız"}

```

go to fscohort/views.py
```python
from django.shortcuts import render, redirect
from .forms import StudentForm

def student_add(request):
    form = StudentForm() # boş form render edeceğiz
    if request.method == 'POST':          
        print(request.POST)				   
        form = StudentForm(request.POST)   
        if form.is_valid():				   
            form.save()
            return redirect("list")					   
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_add.html', context)
```

go to fscohort/urls.py
```python
from django.urls import path
from .views import index, student_list, student_add

urlpatterns = [
    path('', index, name='home'),
    path('list/',student_list , name='list'),
    path('add/',student_add , name='add'),
]
```

student_add.html
```html
{% extends 'fscohort/base.html' %}

{% block container %}
    <h2>Add Student</h2>
    <form action="" method="POST">
        {% csrf_token %}                   
        {{form.as_p}}						   
        <input type="submit" value="add">
    </form>
{% endblock container %}
```

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - UPDATE (POST)       /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to fscohort/views.py
```python
def student_update(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")   
    context = {
        'form':form,
    }
    return render(request, 'fscohort/student_update.html', context)
```

go to fscohort/urls.py
```python
from django.urls import path
from .views import index, student_list, student_add, student_update

urlpatterns = [
    path('', index, name='home'),
    path('list/',student_list , name='list'),
    path('add/',student_add , name='add'),
    path('update/<int:id>',student_update , name='update'),
]
```

student_update.html
```html
{% extends 'fscohort/base.html' %}

{% block container %}
    <h2>Update Student</h2>
    <form action="" method="POST">
        {% csrf_token %}                   
        {{form.as_p}}						   
        <input type="submit" value="update">
    </form>
{% endblock container %}
```


/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - DELETE (POST)       /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to fscohort/views.py
```python
def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")
    return render(request, "fscohort/student_delete.html") 
```

go to fscohort/urls.py
```python
from django.urls import path
from .views import index, student_list, student_add, student_update, student_delete

urlpatterns = [
    path('', index, name='home'),
    path('list/',student_list , name='list'),
    path('add/',student_add , name='add'),
    path('update/<int:id>',student_update , name='update'),
    path('delete/<int:id>',student_delete , name='delete'),
]
```

student_delete.html
```html
{% extends 'fscohort/base.html' %}


{% block container %}
    <form action="" method="POST">
        <p>Are You Sure!</p>
        {% csrf_token %}
        <input type="submit" value="Yes">
    </form>
    <a href="{% url 'list' %}">
        <button>No</button>
    </a>
{% endblock container %}
```

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         STUDENT DETAIL PAGE         /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to fscohort/views.py
```python
def student_detail(request, id):        
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)
```

	go to fscohort/urls.py
```python
from django.urls import path
from .views import index, student_list, student_add, student_update, student_delete, student_detail

urlpatterns = [
    path('', index, name='home'),
    path('list/',student_list , name='list'),
    path('add/',student_add , name='add'),
    path('update/<int:id>',student_update , name='update'),
    path('delete/<int:id>',student_delete , name='delete'),
    path('student/<int:id>', student_detail, name="detail"),
]
```

student_detail.html
```html
{% extends 'fscohort/base.html' %}

{% block container %}
    {{student.number}} - {{student.first_name}} {{student.last_name}}
    <br>
    <a href="{% url 'update' student.id %}"><button>Update</button></a>
    <a href="{% url 'delete' student.id %}"><button>Delete</button></a>
{% endblock container %}
```

go to student_list.html
```html
{% extends 'fscohort/base.html' %}

{% block container %}
<ul>
    {% for student in students%}
    <a href="{% url 'detail' student.id  %}">
    <li>{{ student.number }} - {{student.first_name}} {{student.last_name}}</li>
    </a>
    {%endfor%}
</ul>
{% endblock container %}
```

------------------------------------------------------
add student_list template "student add" button
add student_add template "cancel" button
------------------------------------------------------
### add messages

go to base.html:
```html
        {% if messages %} 
        {% for message in messages %} 
            {% if message.tags == "error" %}
                <div class="alert alert-danger">{{ message }}</div>
            {% else %}
                <div class="alert alert-{{ message.tags }}">{{ message }}</div>
            {% endif %} 
        {% endfor %} 
      {% endif %} 

```

go to views.py:
```python
from django.contrib import messages

            form.save()
            messages.success(request, "student created succesfully!")
            return redirect("list")
```



