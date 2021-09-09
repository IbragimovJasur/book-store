from django.urls import path
from .views import allorders

urlpatterns= [
    path('myorders/', allorders, name='my_orders'),
]
