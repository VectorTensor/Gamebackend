from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



