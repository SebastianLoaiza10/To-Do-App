# Generated by Django 4.2.4 on 2023-08-11 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_priority_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priority',
            name='level',
        ),
    ]
