from django import forms
from .models import Certificate


class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = [
            'student_name',
            'course_name',
            'completion_date'
        ]

        widgets = {
            'completion_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }