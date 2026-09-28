from django.shortcuts import render
from .forms import StudentForm


IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png']


def student_registration(request):

    form = StudentForm()
    message = ''
    error = ''

    if request.method == 'POST':

        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():

            student = form.save(commit=False)

            student.id_card = request.FILES['id_card']

            file_type = student.id_card.name.split('.')[-1].lower()

            if file_type not in IMAGE_FILE_TYPES:

                error = 'Error: Only JPG, JPEG, and PNG files are allowed.'

            else:

                student.save()

                message = 'Student registration saved successfully!'

                form = StudentForm()

    context = {
        'form': form,
        'message': message,
        'error': error
    }

    return render(
        request,
        'studentregistration/student_form.html',
        context
    )