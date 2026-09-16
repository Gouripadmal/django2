from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_customer, name='add_customer'),
    path('all/', views.all_customers, name='all_customers'),
    path('filtered/', views.filtered_customers, name='filtered_customers'),
]