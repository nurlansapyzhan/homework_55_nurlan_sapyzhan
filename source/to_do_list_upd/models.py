from django.db import models


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=200, null=False, blank=False, default='new', verbose_name='Статус')
    finish_date = models.DateField(auto_now=True, verbose_name='Дата выполнения')
    detail_description = models.TextField(max_length=2000, null=True, blank=False, verbose_name='Подробное описание')

    def __str__(self):
        return f'{self.description}, {self.status}, {self.finish_date}'
