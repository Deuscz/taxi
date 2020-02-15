from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'order_add', 'destination_add', 'des_time']