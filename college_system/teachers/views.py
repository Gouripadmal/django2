from django.shortcuts import render, redirect


def teacher_list(request, message):
    teachers = [
        "Dr. Anitha",
        "Prof. Rajesh",
        "Dr. Meena",
        "Prof. Suresh",
        "Dr. Priya"
    ]

    return render(request, 'teachers/teacher_list.html', {
        'teachers': teachers,
        'message': message
    })


def add_teacher(request):
    if request.method == 'POST':
        return redirect('teachers:teacher_list', message='Welcome to the Teacher List')

    return render(request, 'teachers/add_teacher.html')