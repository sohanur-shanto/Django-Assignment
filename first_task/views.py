from django.shortcuts import render
from . permissions import IsProjectManager
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from . models import *
from django.contrib.auth.mixins import PermissionRequiredMixin



@method_decorator(login_required, name='dispatch')
class TaskView(PermissionRequiredMixin, ListView):
    template_name = 'test.html'
    permission_required = 'first_task.view_task'
    permission_classes = [IsProjectManager]
    
    def get_queryset(self):
        queryset = Task.objects.all()       
        user = self.request.user
        if user is not None:
            queryset = queryset.filter(project_manager__user=user)
        return queryset
    

