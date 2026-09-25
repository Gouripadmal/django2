from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add_note/', views.add_note, name='add_note'),
    path('list_notes/', views.list_notes, name='list_notes'),
]