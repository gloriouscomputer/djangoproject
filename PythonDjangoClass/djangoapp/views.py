from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserForm, UserLoginForm
from django.views import  View
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .models import CustomUser

class Homeview(View):
        def get(self, request):
            return render(request, template_name='index.html')


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
                    if user.user_role == 'teacher':
                        return redirect('teacher_dashboard')
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
        return render(request, template_name='Admin-dashboard/dashhome.html')
   
class StudentView(View):
    def get(self, request):
        student_data = CustomUser.objects.filter(user_role='student')
        return render(request, template_name="Admin-dashboard/studentdata.html", context={'student_data': student_data})
    
class RegisterView(View):
    # def get(self, request):
    #     return render(request, template_name="Admin-dashboard/student_register.html")
    """This class write for user registration this will take a request from user """
    form_class = CustomUserForm
    template_name = 'Admin-dashboard/student_register.html'

    def get(self, request):
        """This method write for get user registration form"""
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        """This method write for validate user registration request and save user in database"""
        form = self.form_class(request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                form.save()
                context={'message':'success', 'user_name':username,
                         'password':password,'form': self.form_class}
                return render(request, self.template_name, context=context)

            else:
                return render(request, self.template_name, context={'form': self.form_class})
        except Exception as error:
            return render(request, self.template_name, context={'error': error})
        
class StudentUpdateView(View):
    # def get(self, request):
    #     return render(request, template_name="Admin-dashboard/student_register.html")
    """This class write for user registration this will take a request from user """
    form_class = CustomUserForm
    template_name = 'Admin-dashboard/student_register.html'

    def get(self, request,student_id):
        """This method write for get user registration form"""
        student_data = CustomUser.objects.get(id=student_id)
        return render(request, self.template_name, context={'student_data': student_data})


class BlogView(View):
    def get(self, request):
        return render(request, template_name="Admin-dashboard/dashblog.html")
    
class AddblogView(View):
    def get(self, request):
        return render(request, template_name="Admin-dashboard/addblog.html")

class DashloginView(View):
    def get(self, request):
        return render(request, template_name="Admin-dashboard/dashlogin.html")
    
class SuperadminView(View):
    def get(self, request):
        return render(request, template_name='Admin-dashboard/dashhome.html')