from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list_view, name='task_list'),
    path('tasks/create/', views.task_create_view, name='task_create'),
    path('tasks/<int:task_id>/', views.task_detail_view, name='task_detail'),
    path('tasks/<int:task_id>/update/', views.task_update_view, name='task_update'),
    path('tasks/<int:task_id>/delete/', views.task_delete_view, name='task_delete'),


]

