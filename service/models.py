from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Car(models.Model):
    model = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    car_num = models.CharField(max_length=15, default=None, unique=True)

    class Meta:
        ordering = ['model']

    def __str__(self):
        return self.car_num


class Order(models.Model):
    name_reg = RegexValidator(regex=r'^[А-Яа-я ]{5,50}$',
                              message='The name must be written in Cyrillic and not more than 50 characters!')
    phone_reg = RegexValidator(regex=r'^[+]{1}(380)[(]{0,1}[0-9]{2}[)]{0,1}[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$',
                               message='Phone number must be entered in the format: "+380(XX)XXX-XX-XX" !')
    name = models.CharField(validators=[name_reg], max_length=50)
    phone = models.CharField(validators=[phone_reg], max_length=18)
    order_add = models.CharField(max_length=255)
    destination_add = models.CharField(max_length=255)
    des_time = models.TimeField()
    status = models.CharField(default='Open', max_length=6)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, default=None, blank=True)
    date = models.DateTimeField(auto_created=True, default=timezone.now())

    class Meta:
        ordering = ['-status', '-date']

    def __str__(self):
        return self.phone
