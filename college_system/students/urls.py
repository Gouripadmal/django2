from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('<str:message>/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
]