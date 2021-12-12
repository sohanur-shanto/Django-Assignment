from django.db import models
from django.contrib.auth.models import User


class ProjectManager(models.Model):
    user = models.OneToOneField(User, related_name="project_manager", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
        
class Task(models.Model):
    
    STATUS_CHOICES = [
        ('ASSIGNED', 'Assigned'),
        ('PROCESSING', 'Processing'),
        ('DECLINED', 'Declined'),
        ('CLOSED', 'Closed'),   
    ]
    
    project_manager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title