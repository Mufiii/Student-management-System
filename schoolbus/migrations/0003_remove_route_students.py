# Generated by Django 5.0.4 on 2024-08-03 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schoolbus", "0002_route_students"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="route",
            name="students",
        ),
    ]
