from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('<str:message>/', views.teacher_list, name='teacher_list'),
    path('add/', views.add_teacher, name='add_teacher'),
]