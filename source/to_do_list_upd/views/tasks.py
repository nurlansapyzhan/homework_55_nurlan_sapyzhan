from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from to_do_list_upd.models import Task


def add_task(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'finish_date': request.POST.get('finish_date'),
        'detail_description': request.POST.get('detail_description')
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def delete_task(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'index.html')
    task_pk = request.POST.get('pk')
    task = Task.objects.get(pk=task_pk)
    task.delete()
    return redirect('index')


def detail_view(request: WSGIRequest, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', context={'task': task})
