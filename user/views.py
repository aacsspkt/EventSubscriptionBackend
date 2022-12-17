from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from user import serializers, models, permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and upating user profiles"""
    serializer_class = serializers.UserProfileSerializer

    #get all objects from db
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

