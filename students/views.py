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