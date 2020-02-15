# Generated by Django 2.2.6 on 2020-02-14 17:31

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['username'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: "+380(XX)XXX-XX-XX" !', regex='^[+]{1}(380)[(]{0,1}[0-9]{2}[)]{0,1}[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$')])),
                ('order_add', models.CharField(max_length=255)),
                ('destination_add', models.CharField(max_length=255)),
                ('des_time', models.TimeField()),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='service.Car')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]