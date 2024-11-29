from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializer import CourseSerializer,CourseDetailSerializer,UserSerializer
from rest_framework import generics, filters
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend


class CourseListCreateView(generics.ListCreateAPIView):
    
    serializer_class=CourseSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['course_name']
    filterset_fields = ['price', 'discount']
    queryset=Course.objects.all()
    
    
class CourseDetails(generics.RetrieveAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseDetailSerializer
    lookup_field='id'


class CourseList(ListAPIView):
    pass
    
    
class CourseUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all() 
    serializer_class = CourseDetailSerializer 
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):
        serializer.save() 

    def perform_destroy(self, instance):
        instance.delete() 

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



from rest_framework.authtoken.models import Token


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response({"message": "Login successful", "token": token.key}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

