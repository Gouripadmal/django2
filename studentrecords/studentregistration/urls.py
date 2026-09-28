from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_registration, name='student_registration'),
]