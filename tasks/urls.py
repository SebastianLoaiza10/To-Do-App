from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ViewTasks, name = 'task_list'),
    path('task-create/', views.CreateTask, name = 'create_task'),
    path('update/<int:task_id>/', views.UpdateTask, name = "update_task"),
    path('delete/<int:task_id>/', views.DeleteTask, name = "delete_task"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.searchTask, name='search_tasks'),
]