# Generated by Django 5.1.1 on 2024-10-01 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='tittle',
            new_name='title',
        ),
    ]
