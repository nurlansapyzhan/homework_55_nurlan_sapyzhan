from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from to_do_list_upd.models import Task

from to_do_list_upd.forms import TaskForm


def add_task(request: WSGIRequest):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})
    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'task_create.html', context={'form': form})
    else:
        task = Task.objects.create(**form.cleaned_data)
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


def edit_task(request: WSGIRequest, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'description': task.description,
            'status': task.status,
            'finish_date': task.finish_date,
            'detail_description': task.detail_description
        })
        return render(request, 'task_edit.html', context={'task': task, 'form': form})
    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'task_edit.html', context={'task': task, 'form': form})
    else:
        task.description = form.cleaned_data['description']
        task.status = form.cleaned_data['status']
        task.finish_date = form.cleaned_data['finish_date']
        task.detail_description = form.cleaned_data['detail_description']
        task.save()
        return redirect('task_detail', task.pk)


