from django.contrib import admin

from to_do_list_upd.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'finish_date')
    list_filter = ('id', 'description', 'status', 'finish_date')
    search_fields = ('status', 'finish_date')
    fields = ('id', 'description', 'status', 'finish_date')
    readonly_fields = ('id', 'finish_date')


admin.site.register(Task, TaskAdmin)
