from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_list_upd.models import Task


def add_task(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'finish_date': request.POST.get('finish_date')
    }
    Task.objects.create(**task_data)
    return redirect('/')


def delete_task(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'index.html')
    task_pk = request.POST.get('pk')
    print(task_pk)
    task = Task.objects.get(pk=task_pk)
    task.delete()
    return redirect('/')


def edit_task(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'finish_date': request.POST.get('finish_date')
    }
    task = Task(**task_data)
    task.save()
    return redirect('/')


def detail_view(request:WSGIRequest):
    task_pk = request.GET.get('pk')
    task = Task.objects.get(pk=task_pk)
    context = {'task': task}
    task.delete()
    return render(request, 'task.html', context=context)
