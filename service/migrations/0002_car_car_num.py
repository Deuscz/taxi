# Generated by Django 2.2.6 on 2020-02-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_num',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
