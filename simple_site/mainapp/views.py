from django.shortcuts import render


def home(request):
    return render(request, 'mainapp/home.html')


def about(request):
    return render(request, 'mainapp/about.html')