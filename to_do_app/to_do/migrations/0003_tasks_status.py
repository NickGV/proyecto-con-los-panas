# Generated by Django 5.1.1 on 2024-10-31 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_rename_tittle_tasks_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
