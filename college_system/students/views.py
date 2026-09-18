from django.shortcuts import render, redirect


def student_list(request, message):
    students = [
        "Anu",
        "Arun",
        "Meera",
        "Rahul",
        "Sneha"
    ]

    return render(request, 'students/student_list.html', {
        'students': students,
        'message': message
    })


def add_student(request):
    if request.method == 'POST':
        return redirect('students:student_list', message='Welcome to the Student List')

    return render(request, 'students/add_student.html')