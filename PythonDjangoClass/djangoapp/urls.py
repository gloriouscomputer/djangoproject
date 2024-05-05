
from django.urls import path
from .views import  *


urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]