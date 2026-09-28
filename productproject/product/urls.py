from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.add_product,
        name='add_product'
    ),

    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'product/<int:product_id>/pdf/',
        views.download_pdf,
        name='download_pdf'
    ),

    path(
        'product/<int:product_id>/email/',
        views.send_email,
        name='send_email'
    ),
]