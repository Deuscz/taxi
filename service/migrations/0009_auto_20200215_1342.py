# Generated by Django 2.2.6 on 2020-02-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='car',
        ),
        migrations.AddField(
            model_name='order',
            name='car',
            field=models.ManyToManyField(to='service.Car'),
        ),
    ]