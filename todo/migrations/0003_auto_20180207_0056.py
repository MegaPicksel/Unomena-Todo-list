# Generated by Django 2.0 on 2018-02-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todolist_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='Done',
            field=models.BooleanField(),
        ),
    ]
