# Generated by Django 5.1.2 on 2025-01-31 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('pid', models.IntegerField()),
                ('units', models.IntegerField()),
                ('unitprice', models.DecimalField(decimal_places=4, max_digits=10)),
                ('tuprice', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pcat', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('prodid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='productapp.product')),
                ('tot_qty', models.IntegerField()),
                ('last_update', models.DateField()),
                ('next_update', models.DateField()),
            ],
        ),
    ]
