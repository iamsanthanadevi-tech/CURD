# EX.No: 03 DEVELOP A DJANGO-BASED CRUD APPLICATION
## Date: 24-11-2026
## AIM

To develop a Django-based web application that performs CRUD (Create, Read, Update, and Delete) operations on student records.

## ALGORITHM

1. Create a Django project and an application.
2. Define the `Student` model with the required fields (Name and Email).
3. Run migrations to create the database table.
4. Configure URL routing for Home, Add, Update, and Delete operations.
5. Create the `home()` view to retrieve and display all student records.
6. Create the `add()` view to insert a new student record into the database.
7. Create the `update()` view to modify an existing student record using its ID.
8. Create the `delete()` view to remove a student record using its ID.
9. Design the HTML page with separate forms/buttons for Add, View, Update, and Delete operations.
10. Run the Django development server and perform all CRUD operations through the web browser.

## PROGRAM

# EX.NO: 03 DEVELOP A DJANGO-BASED CRUD APPLICATION

# 1. models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


# 2. views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Read - Display students
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


# Create - Add student
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        Student.objects.create(
            name=name,
            email=email
        )
        return redirect('home')

    return render(request, 'add_student.html')


# Update - Edit student
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.save()

        return redirect('home')

    return render(request, 'edit_student.html', {'student': student})


# Delete - Remove student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')


# 3. students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
]


# 4. studentmanagement/urls.py

from django.urls import path, include

urlpatterns = [
    path('', include('students.urls')),
]




## OUTPUT
<img width="1798" height="973" alt="Screenshot 2026-11-24 231042" src="https://github.com/user-attachments/assets/2dabd6c8-b895-4611-ad7b-4d969cf6d846" />



## RESULT

A Django-based CRUD web application was successfully developed to perform Create, Read, Update, and Delete operations on student records using SQLite as the backend database.


