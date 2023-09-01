# Generated by Django 4.2.4 on 2023-08-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_priority_alter_task_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed', '-priority', 'due_date']},
        ),
        migrations.AddField(
            model_name='priority',
            name='level',
            field=models.IntegerField(choices=[(3, 'High'), (2, 'Medium'), (1, 'Low')], default=3),
        ),
    ]
