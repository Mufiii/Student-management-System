# Generated by Django 5.0.4 on 2024-05-31 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_no', models.PositiveSmallIntegerField(unique=True)),
                ('driver_name', models.CharField(blank=True, max_length=150, null=True)),
                ('plate_number', models.CharField(blank=True, max_length=15, null=True)),
                ('capacity', models.PositiveIntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_no', models.PositiveSmallIntegerField()),
                ('from_location', models.CharField(max_length=255)),
                ('to_location', models.CharField(max_length=255)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='schoolbus.bus')),
            ],
            options={
                'unique_together': {('bus', 'route_no')},
            },
        ),
        migrations.CreateModel(
            name='BusPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_points', to='schoolbus.route')),
            ],
        ),
    ]
