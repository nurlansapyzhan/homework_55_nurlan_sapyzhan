# Generated by Django 4.1.7 on 2023-02-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_upd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detail_description',
            field=models.TextField(max_length=2000, null=True, verbose_name='Подробное описание'),
        ),
    ]
