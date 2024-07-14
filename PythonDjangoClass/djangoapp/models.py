from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

class TimeStap(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    modification_at = models.DateTimeField(auto_now_add=True)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser,TimeStap):

    USERROLE = (
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("admin", "Admin"),
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_role = models.CharField(max_length=255, choices=USERROLE, default='admin')
    # Additional fields as per your requirements

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username



class Blog(models.Model):
    name = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to='media/image', null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Student(TimeStap):
    username = models.CharField(max_length=255, null=False, blank=False)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)
    phone = models.IntegerField( null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.email