# Generated by Django 4.2.4 on 2023-08-11 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': [models.Case(models.When(completed=True, then=models.Value(1)), default=models.Value(0), output_field=models.BooleanField()), '-priority', 'due_date']},
        ),
        migrations.AlterField(
            model_name='priority',
            name='level',
            field=models.IntegerField(choices=[(3, 'High'), (2, 'Medium'), (1, 'Low')]),
        ),
    ]
