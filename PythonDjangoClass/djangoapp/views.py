from django.http import HttpResponse
from django.shortcuts import render
from .models import Student,CustomUser
from .forms import StudentForm, CustomUserForm, UserLoginForm
from django.views import  View
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
# Create your views here.


class Homeview(View):
        def get(self, request):
            return render(request, template_name='index.html')


def registration(request):
        if request.method =='GET':
                form = CustomUserForm()
                return render(request, template_name='registrations.html', context={'form':form})
        if request.method == 'POST':
                form  = CustomUserForm(request.POST)
                if form.is_valid():
                        form.save()
                        return render(request, template_name='registrations.html', context={'form':form})
                return render(request, template_name='registrations.html', context={'error':'Invalid data', 'form':form})


# This is registration form
class Register(View):
    """This class write for user registration this will take a request from user """
    form_class = CustomUserForm
    template_name = 'registrations.html'

    def get(self, request):
        """This method write for get user registration form"""
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        """This method write for validate user registration request and save user in database"""
        form = self.form_class(request.POST)
        try:
            if form.is_valid():
                form.save()
                context={'message':'success'}
                return redirect('index', context=context)
            else:
                return render(request, self.template_name, context={'form': self.form_class})
        except Exception as error:
            return render(request, self.template_name, context={'error': error})


class LoginView(View):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get(self, request):
        return render(request, 'login.html', {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    return redirect('home')
                else:
                    return HttpResponse("Your account is disabled.")
            else:
                return HttpResponse("Invalid login credentials.")
        else:
            return render(request, self.template_name, {'form': form})


class AboutView(View):
    def get(self, request):
        return render(request, template_name='about.html')

class BlogView(View):
    def get(self, request):
        return render(request, template_name='blog.html')
    
class ContactView(View):
    def get(self, request):
        return render(request, template_name='contact.html')

class CourseView(View):
    def get(self, request):
        return render(request, template_name='course.html')

class SingleView(View):
    def get(self, request):
        return render(request, template_name='single.html')

class TeacherView(View):
    def get(self, request):
        return render(request, template_name='teacher.html')
    
class DashboardView(View):
    def get(self, request):
        return render(request, template_name='Admin-dashboard/dashboard.html')