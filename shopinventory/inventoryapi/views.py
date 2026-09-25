from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


# CREATE + READ
@api_view(['GET', 'POST'])
def products(request):

    # CREATE PRODUCT
    if request.method == 'POST':

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # READ ALL PRODUCTS
    if request.method == 'GET':

        products = Product.objects.all()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(serializer.data)


# UPDATE + DELETE
@api_view(['PUT', 'DELETE'])
def product_detail(request, pk):

    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return Response(
            {'error': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    # UPDATE PRODUCT
    if request.method == 'PUT':

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE PRODUCT
    if request.method == 'DELETE':

        product.delete()

        return Response(
            {'message': 'Product deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )