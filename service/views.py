from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .forms import OrderForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# View for taxi ordering
class OrderView(TemplateView):
    template_name = 'order.html'

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            cars = Car.objects.filter(available=True)
            if cars:
                car = cars[0]
                car.available = False
                car.save()
                order = Order.objects.create(**form.cleaned_data, car=car)
                return render(request, 'order_info.html', {'order': order})
            else:
                messages.add_message(request, messages.INFO,
                                     'There is no cars available!')
        else:
            messages.add_message(request, messages.INFO,
                                 'Your order has incorrect values!')
        return render(request, 'order.html', {})


# Login view
class LoginLogoutView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                messages.add_message(request, messages.INFO,
                                     'There is no user with such credentials!')
        return render(request, 'login.html', {})


# Authenticated order list
class Order_List(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/orders/'
    model = Order
    template_name = 'order_list.html'
    paginate_by = 5


# Authenticated order details
class Order_Detail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = '/orders/'
    model = Order
    template_name = 'order_detail.html'


# Order closing and car release
@login_required
def order_close(request, pk):
    if request.method == 'POST':
        order = Order.objects.get(pk=pk)
        order.status = 'Closed'
        car = order.car
        car.available = True
        car.save()
        order.save()
    return redirect('list')
