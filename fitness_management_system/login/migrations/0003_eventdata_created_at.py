# Generated by Django 4.1.2 on 2022-11-11 04:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_duration_eventdata_exercise_times_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdata',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
