from django import forms
from django.forms import ModelForm
from .models import Task 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # finds out what model the form is going to be based on
        fields = ['title', 'description', 'due_date', 'completed'] # includes all the fields from the Task class created in Models.py
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')