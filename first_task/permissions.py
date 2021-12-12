from . models import *
from rest_framework.permissions import BasePermission


class IsProjectManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.project_manager:
            return True
        else:
            return False