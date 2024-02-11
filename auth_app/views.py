from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import UserSignupSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # Authenticate user
    if username:
        user = authenticate(username=username, password=password)
        token = Token.objects.get(user=user)
    elif email:
        user = authenticate(email=email, password=password)
        token = Token.objects.get(user=user)
    
    if user is not None:
        return Response({'user': 'Login successful', 'Token':f'{token}'}, status=status.HTTP_200_OK)
    else:
        # If user authentication fails, return error response
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserSignupAPIView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            # Save the validated data to create a new user
            user = serializer.save()    
            # Create a token for the new user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'Token':str(token), 'serializer_data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)