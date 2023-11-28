from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def ViewTasks(request):
    tasks = Task.objects.filter(user=request.user) # Query all the users tasks from the database
    incomplete_tasks = Task.objects.filter(user=request.user, completed=False)  # Query incomplete tasks
    context = {
        'tasks': tasks,
        'incomplete_tasks': incomplete_tasks,
    }  # Create a context dictionary with the 'tasks'& 'incomplete_tasks' queryset
    return render(request, 'tasks/list.html', context) # Render the 'list.html' template with the context data

@login_required
def CreateTask(request):
    form = TaskForm()
    if request.method == 'POST': # checks if the HTTP request is wanting to submit data
        form = TaskForm(request.POST) # Passes the data in the TaskForm
        if form.is_valid(): # Checks to see if the data is valid based on the rules of TaskForm 
            form.save() # Saves the data from the form into the database
            return redirect('task_list') # Redirect to the task list view
        else: # incase user input incorrect data
            form = TaskForm() 
    context = {'form': form} # To provide the data for the templete when rendering
    return render(request, 'tasks/create_task.html', context)

@login_required
def UpdateTask(request, task_id):
    task = Task.objects.get(id = task_id) # creates variable to query the specific task based on the field id, which is the primary key
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) # takes the task's data into the form and replaces it with user given data
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task) # keeps the form the exact same
    context = {'form': form, 'task': task}
    return render(request, 'tasks/update_task.html', context) # provides user with the fields filled with the data they provided for that task before

@login_required
def searchTask(request):
    form = SearchForm(request.GET)
    tasks = [] # Will make a list for the searched tasks

    if form.is_valid():
        query = form.cleaned_data['query'] # get the users input search
        if query:
            tasks = Task.objects.filter(title__icontains=query)  # Perform the search query
    else: # isn't valid if the search is blank
        tasks = Task.objects.filter(user=request.user) # If the search is empty
    
    context = {'form': form, 'tasks': tasks}
    return render(request, 'tasks/list.html', context)

@login_required
def DeleteTask(request, task_id):
    task = Task.objects.get(id = task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    context = {'task': task}
    return render(request, 'tasks/delete_task.html', context)
