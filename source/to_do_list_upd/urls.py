from django.urls import path

from to_do_list_upd.views.base import index_view

from to_do_list_upd.views.tasks import add_task, delete_task, detail_view, edit_task

urlpatterns = [
    path('', index_view),
    path('task/', index_view),
    path('task/add/', add_task),
    path('task/delete/', delete_task),
    path('task/<int:pk>', detail_view, name='detail_view'),
    path('task/edit/', edit_task)
]
