# Generated by Django 5.0.4 on 2024-08-03 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_student_route"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="route",
        ),
    ]