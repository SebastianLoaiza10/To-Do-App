from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    # title of the task
    title = models.CharField(max_length=200) 

    # description of the task
    description = models.TextField() 

    # creates the one to many relationship so that a user can have multiple tasks assigned to them
    # CASCADE makes it to where if the user is deleted, then it will delete the tasks assigned to the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # this will take the time and date that the task was created by the user
    created_at = models.DateTimeField(auto_now_add=True)

    # This will hold the date the user made the certain task be due
    due_date = models.DateField()

    # This will make the created task not completed initially
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    # This makes the ordering of the tasks to be sorted by having the completed tasks at the bottom
    class Meta():
        ordering = ['completed']