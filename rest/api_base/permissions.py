from rest_framework import permissions
from django.http import HttpResponse
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
 

class  IsAuthenticated(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method not in SAFE_METHODS:
            return HttpResponse('Article not found!')