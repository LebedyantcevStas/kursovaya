# Generated by Django 5.0 on 2024-02-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_contactphone_delete_order_gym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adress',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_shipping',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_shipping',
            field=models.TextField(null=True),
        ),
    ]