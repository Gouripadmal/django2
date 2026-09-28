from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from reportlab.pdfgen import canvas

from .models import Product
from .forms import ProductForm


# Add Product
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save()

            return redirect(
                'product_detail',
                product_id=product.id
            )

    else:
        form = ProductForm()

    return render(
        request,
        'product/add_product.html',
        {'form': form}
    )


# Display Product Details
def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'product/product_detail.html',
        {'product': product}
    )


# Download Product Details as PDF
def download_pdf(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="{product.name}.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.drawString(100, 750, "Product Details")
    pdf.drawString(100, 700, f"Name: {product.name}")
    pdf.drawString(100, 650, f"Description: {product.description}")
    pdf.drawString(100, 600, f"Price: {product.price}")

    pdf.save()

    return response


# Send Product Details by Email
def send_email(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    subject = f"Product Information - {product.name}"

    message = f"""
Product Details

Name: {product.name}

Description: {product.description}

Price: {product.price}
"""

    send_mail(
        subject,
        message,
        'yourgmail@gmail.com',
        ['yourgmail@gmail.com'],
    )

    return redirect(
        'product_detail',
        product_id=product.id
    )