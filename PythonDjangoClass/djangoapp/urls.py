
from django.urls import path
from .views import  *



urlpatterns = [
    path('', student, name='home'),
    path('index/', StudentView.as_view(), name='index'),
    path('register/', registration, name='register'),
    path('sign-in/', Register.as_view(), name='sign-in'),
    path('login/', login, name='login')
]