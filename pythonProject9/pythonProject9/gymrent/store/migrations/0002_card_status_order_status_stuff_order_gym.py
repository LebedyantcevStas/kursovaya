# Generated by Django 5.0 on 2023-12-19 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='order_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_num', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuff_num', models.CharField(max_length=15)),
                ('stuff_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order_gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('plan_return_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('forfeit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stuff', models.IntegerField()),
                ('model_e', models.ManyToManyField(to='store.product')),
                ('status_int', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order_status')),
            ],
        ),
    ]
