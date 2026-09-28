from django.shortcuts import render
from django.http import HttpResponse
from .forms import TeacherForm


IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png']


def create_teacher(request):

    form = TeacherForm()

    if request.method == 'POST':

        form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():

            teacher = form.save(commit=False)

            teacher.profile_photo = request.FILES['profile_photo']

            file_type = teacher.profile_photo.name.split('.')[-1].lower()

            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse(
                    'Error: Only JPG, JPEG, and PNG images are allowed.'
                )

            teacher.save()

            return HttpResponse(
                'Teacher profile saved successfully!'
            )

    context = {
        'form': form
    }

    return render(
        request,
        'teacherprofile/teacher_form.html',
        context
    )