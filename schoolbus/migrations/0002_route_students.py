# Generated by Django 5.0.4 on 2024-08-03 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolbus", "0001_initial"),
        ("student", "0005_remove_student_route"),
    ]

    operations = [
        migrations.AddField(
            model_name="route",
            name="students",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="student.student",
            ),
        ),
    ]
