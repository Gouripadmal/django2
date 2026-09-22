from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            request.session['visit_count'] = 0

            return redirect('welcome')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def welcome(request):

    if 'visit_count' in request.session:
        request.session['visit_count'] += 1
    else:
        request.session['visit_count'] = 1

    count = request.session['visit_count']

    return render(request, 'welcome.html', {'count': count})


@login_required(login_url='/login/')
def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return render(request, 'logout.html')