from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Note
from .serializers import NoteSerializer


# SIGNUP
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {'error': 'Username and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password
    )

    return Response(
        {'message': 'User created successfully'},
        status=status.HTTP_201_CREATED
    )


# LOGIN
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'username': user.username,
            'token': token.key
        })

    return Response(
        {'error': 'Invalid username or password'},
        status=status.HTTP_401_UNAUTHORIZED
    )


# ADD NOTE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_note(request):

    title = request.data.get('title')
    message = request.data.get('message')

    if not title or not message:
        return Response(
            {'error': 'Title and message are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    note = Note.objects.create(
        user=request.user,
        title=title,
        message=message
    )

    serializer = NoteSerializer(note)

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )


# LIST NOTES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notes(request):

    notes = Note.objects.filter(user=request.user)

    serializer = NoteSerializer(
        notes,
        many=True
    )

    return Response(serializer.data)