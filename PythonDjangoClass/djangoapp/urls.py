
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

    path('teacher_dashboard/', DashboardView.as_view(), name='teacher_dashboard'),
    path('superadmin/', SuperadminView.as_view(), name='superadmin'),
    path('studentdata/', StudentView.as_view(), name='studentdata'),
    path('student_register/', RegisterView.as_view(), name='student_register'),
    path('student/<int:student_id>', StudentUpdateView.as_view(), name='student_update'),
    path('blog/',BlogView.as_view(), name='blog'),
    path('addblog/', AddblogView.as_view(), name='addblog'),
    path('login/', DashloginView.as_view(), name='dashlogin')
]