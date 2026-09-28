from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from reportlab.pdfgen import canvas

from .models import Certificate
from .forms import CertificateForm


# Add Certificate
def add_certificate(request):

    if request.method == 'POST':

        form = CertificateForm(request.POST)

        if form.is_valid():

            certificate = form.save()

            return redirect(
                'certificate_detail',
                certificate_id=certificate.id
            )

    else:

        form = CertificateForm()

    return render(
        request,
        'certificate/add_certificate.html',
        {'form': form}
    )


# Display Certificate Details
def certificate_detail(request, certificate_id):

    certificate = get_object_or_404(
        Certificate,
        id=certificate_id
    )

    return render(
        request,
        'certificate/certificate_detail.html',
        {'certificate': certificate}
    )


# Generate and Download PDF
def download_certificate(request, certificate_id):

    certificate = get_object_or_404(
        Certificate,
        id=certificate_id
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="{certificate.student_name}_certificate.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.drawString(
        200,
        750,
        "CERTIFICATE OF COMPLETION"
    )

    pdf.drawString(
        100,
        680,
        f"Student Name: {certificate.student_name}"
    )

    pdf.drawString(
        100,
        630,
        f"Course: {certificate.course_name}"
    )

    pdf.drawString(
        100,
        580,
        f"Completion Date: {certificate.completion_date}"
    )

    pdf.drawString(
        100,
        500,
        "Congratulations on successfully completing the course!"
    )

    pdf.save()

    return response


# Send Certificate Details by Email
def send_certificate_email(request, certificate_id):

    certificate = get_object_or_404(
        Certificate,
        id=certificate_id
    )

    subject = (
        f"Certificate of Completion - "
        f"{certificate.course_name}"
    )

    message = f"""
Dear {certificate.student_name},

Congratulations!

You have successfully completed the course.

Course: {certificate.course_name}
Completion Date: {certificate.completion_date}

Your certificate has been generated.

Thank you.
"""

    send_mail(
        subject,
        message,
        'yourgmail@gmail.com',
        ['student@gmail.com'],
    )

    return redirect(
        'certificate_detail',
        certificate_id=certificate.id
    )