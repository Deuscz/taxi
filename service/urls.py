from django.urls import path
from .views import *
urlpatterns = [
    path('', OrderView.as_view(), name='order'),
    path('login/', LoginLogoutView.as_view(), name='login'),
    path('orders/', Order_List.as_view(), name='list'),
    path('detail/<int:pk>', Order_Detail.as_view(), name='detail'),
    path('detail/<int:pk>/close', order_close, name='close'),
]
