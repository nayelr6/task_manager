from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    priorityChoices=[('low','Low'),('medium','Medium'),('high','High')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    complete = models.BooleanField(default=False)
    priority = models.CharField(max_length = 15,choices= priorityChoices)
    


class TaskPhoto(models.Model):
    task = models.ForeignKey(Task, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='task_photos/')