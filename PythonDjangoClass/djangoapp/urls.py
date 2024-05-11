
from django.urls import path
from .views import  *


urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('Course/', CourseView.as_view(), name='course'),
    path('single/', SingleView.as_view(), name='single'),
    path('teacher/', TeacherView.as_view(), name='teacher'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]