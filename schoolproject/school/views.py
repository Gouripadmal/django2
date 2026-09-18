from django.shortcuts import render

def home(request):
    students = [
        "Anu",
        "Arun",
        "Meera",
        "Rahul",
        "Sneha"
    ]

    return render(request, 'school/home.html', {
        'students': students
    })


def result(request, student_name):
    results = {
        "Anu": "A Grade",
        "Arun": "B Grade",
        "Meera": "A+ Grade",
        "Rahul": "B+ Grade",
        "Sneha": "A Grade"
    }

    student_result = results.get(student_name, "Result not found")

    return render(request, 'school/result.html', {
        'student_name': student_name,
        'student_result': student_result
    })