from django.urls import path

from to_do_list_upd.views.base import index_view

from to_do_list_upd.views.tasks import add_task, delete_task, detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/', index_view),
    path('task/add/', add_task, name='task_add'),
    path('task/delete/', delete_task, name='task_delete'),
    path('task/<int:pk>', detail_view, name='task_detail'),
]
