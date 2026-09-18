from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<str:student_name>/', views.result, name='result'),
]