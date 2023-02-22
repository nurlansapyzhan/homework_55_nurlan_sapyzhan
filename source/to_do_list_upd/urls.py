from django.urls import path

from to_do_list_upd.views.base import index_view

from to_do_list_upd.views.tasks import add_task, delete_task, detail_view, edit_task, confirm_delete

urlpatterns = [
    path('', index_view, name='index'),
    path('task/', index_view),
    path('task/add/', add_task, name='task_add'),
    path('task/<int:pk>', detail_view, name='task_detail'),
    path('task/<int:pk>/edit', edit_task, name='task_edit'),
    path('task/<int:pk>/delete', delete_task, name='task_delete'),
    path('task/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete')
]
