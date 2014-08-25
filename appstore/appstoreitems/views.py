from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    model = User


class GroupViewSet(viewsets.ModelViewSet):
    model = Group


class PermissionViewSet(viewsets.ModelViewSet):
    model = Permission


class ContentTypeViewSet(viewsets.ModelViewSet):
    model = ContentType
