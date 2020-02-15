from django.test import TestCase
from .models import Order, Car
from django.utils import timezone


class CarTest(TestCase):
    def test_car_creation(self):
        self.assertEqual(len(Car.objects.all()), 0)
        car = Car(model='Nissan', available=True, car_num='1564')
        car.save()
        self.assertEqual(len(Car.objects.all()), 1)


class OrderTest(TestCase):

    def setUp(self) -> None:
        car = Car(model='Nissan', available=True, car_num='1564')
        car.save()

    def test_order_creation(self):
        self.assertEqual(len(Order.objects.all()), 0)
        car = Car.objects.all()[0]
        order = Order(name='Иван', phone='+380(97)076-59-34', order_add='Шевченка',
                      destination_add='Олимпийская',
                      des_time=timezone.now(),
                      car=car)
        order.save()
        self.assertEqual(len(Order.objects.all()), 1)
        order = Order.objects.all()[0]
        self.assertEqual(order.name, 'Иван')
        self.assertEqual(order.destination_add, 'Олимпийская')
