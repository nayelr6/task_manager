from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Task, TaskPhoto
from .forms import TaskForm, TaskPhotoForm


# Task List View with Search and Filtering
@login_required
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def task_list_view(request):
    query = request.GET.get('q')
    created_date = request.GET.get('created_date')
    due_date = request.GET.get('due_date')
    priority = request.GET.get('priority')
    complete = request.GET.get('complete')

    #tasks = Task.objects.filter(user=request.user)
    tasks = Task.objects.all()

    if query:
        tasks = tasks.filter(title__icontains=query)

    if created_date:
        tasks = tasks.filter(created_at=created_date)

    if due_date:
        tasks = tasks.filter(due_date=due_date)

    if priority:
        tasks = tasks.filter(priority=priority)

    if complete:
        tasks = tasks.filter(complete=complete)

    return Response({'tasks': tasks}, template_name='task_list.html')


@login_required
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return Response({'task': task}, template_name='task_detail.html')


@login_required
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.data)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return Response({'form': form}, template_name='task_form.html')


@login_required
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def task_update_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.data, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return Response({'form': form}, template_name='task_form.html')


@login_required
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def task_delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return Response({'task': task}, template_name='task_confirm_delete.html')




