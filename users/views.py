from django.shortcuts import render
from .models import CustomUser

def showprofiledata(request):
    user_data= CustomUser.objects.get(id= request.user.id)
    context= {'user_data': user_data}
    return render(request, 'account/profile.html', context)
