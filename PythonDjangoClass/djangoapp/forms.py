from django import forms
from .models import Student,CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ["username",'password', 'user_role']

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        username = self.cleaned_data["username"]
        user.username = f'{username}_gcec'
        user.set_password(password)  # or use make_password(password)
        if commit:
            user.save()
        return user


# class UserLoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)






