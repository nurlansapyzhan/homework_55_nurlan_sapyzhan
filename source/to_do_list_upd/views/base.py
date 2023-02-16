from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_list_upd.models import Task


def index_view(request: WSGIRequest):
    tasks = Task.objects.all()
    for task in tasks:
        print(task)
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)
