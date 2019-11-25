# from django.shortcuts import render
# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializers import UserSerializers, GroupSerializer

class UserViewSet(viewsets.ModelViewset):
    """
    API endpoint that allows users to be views or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer