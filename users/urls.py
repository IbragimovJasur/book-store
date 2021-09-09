from django.urls import path
from .views import showprofiledata

urlpatterns= [
    path('profile/', showprofiledata, name='profile_data'),
]



