from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    form = UserCreationForm(data=request.data)

    if form.is_valid():
        user = form.save()

        return Response(
            {
                "message": "Account created successfully"
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        form.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response(
            {
                "error": "Please provide username and password"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(
        username=username,
        password=password
    )

    if user is None:
        return Response(
            {
                "error": "Invalid username or password"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    token, created = Token.objects.get_or_create(user=user)

    return Response(
        {
            "name": user.username,
            "token": token.key
        },
        status=status.HTTP_200_OK
    )