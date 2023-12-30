from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserUpdateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User



@api_view(['GET', 'POST'])
def user_registration_view(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

       
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)


        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        

        return redirect('user_login') 


    return render(request, 'register.html')

#@api_view(['POST'])
@api_view(['GET','POST'])
def user_login_view(request):
    """
    User login view.
    """
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            #return Response({'message': 'User logged in successfully!'}, status=status.HTTP_200_OK)
            return redirect('task_list')
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return render(request,'login.html')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info_view(request):
    """
    Get authenticated user information view.
    """
    user = request.user
    user_details = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return Response(user_details, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user  
    serializer = UserUpdateSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()  
        return Response({'message': 'User profile updated successfully.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user  


    user.delete()

    return Response({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):

    user_token = Token.objects.get(user=request.user)
    

    user_token.delete()
    
    #return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
    redirect('homepage')
