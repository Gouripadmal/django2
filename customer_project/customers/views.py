from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer


def add_customer(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('all_customers')

    else:
        form = CustomerForm()

    return render(request, 'customers/add_customer.html', {'form': form})


def all_customers(request):

    customers = Customer.objects.all().order_by('name')

    return render(
        request,
        'customers/all_customers.html',
        {'customers': customers}
    )


def filtered_customers(request):

    customers = Customer.objects.filter(
        email__endswith='@example.com'
    ).order_by('name')

    return render(
        request,
        'customers/filtered_customers.html',
        {'customers': customers}
    )