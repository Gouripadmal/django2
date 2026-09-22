from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    query = request.GET.get('search')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {
        'student': students,
        'query': query
    })


def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        student_class = request.POST['student_class']
        age = request.POST['age']

        Student.objects.create(
            name=name,
            student_class=student_class,
            age=age
        )

        return redirect('student_list')

    return render(request, 'students/add_student.html')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.student_class = request.POST['student_class']
        student.age = request.POST['age']

        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {
        'student': student
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/delete_student.html', {
        'student': student
    })