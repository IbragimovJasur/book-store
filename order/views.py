from django.shortcuts import render
from .models import Order

def allorders(request):
    user_id= request.user.id
    all_orders= Order.objects.filter(ordered_by_id=user_id)
    context= {'all_orders': all_orders}
    return render(request, 'order/order_list.html', context)
