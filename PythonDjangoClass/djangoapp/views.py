from django.shortcuts import render
from .models import Student,CustomUser
from .forms import StudentForm, CustomUserForm, UserLoginForm
from django.views import  View
# Create your views here.


def student(request):
        student = Student.objects.all()
        print('student', student)
        return render(request, template_name='index.html')

class StudentView(View):
    template_name = "index.html"
    def get(self, request):
        return render(request, self.template_name)


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











from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'login.html', context={'form':form})

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            breakpoint()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})



class Login(View):

    form_class = UserLoginForm
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')
            return render(request, self.template_name, self.form_class)