from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.add_certificate,
        name='add_certificate'
    ),

    path(
        'certificate/<int:certificate_id>/',
        views.certificate_detail,
        name='certificate_detail'
    ),

    path(
        'certificate/<int:certificate_id>/download/',
        views.download_certificate,
        name='download_certificate'
    ),

    path(
        'certificate/<int:certificate_id>/email/',
        views.send_certificate_email,
        name='send_certificate_email'
    ),
]