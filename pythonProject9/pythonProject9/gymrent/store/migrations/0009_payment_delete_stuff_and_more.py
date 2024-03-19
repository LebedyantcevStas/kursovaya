# Generated by Django 5.0 on 2024-02-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='stuff',
        ),
        migrations.RenameField(
            model_name='order_status',
            old_name='status_num',
            new_name='status_name',
        ),
    ]