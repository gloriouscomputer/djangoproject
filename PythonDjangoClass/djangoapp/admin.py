from django.contrib import admin

# Register your models here.

from .models import CustomUser, Blog, Student

class CustomUserAdmin(admin.ModelAdmin):
    fields = ['first_name','email', 'last_name', 'is_active', 'is_staff', 'is_superuser']

class AdminBlog(admin.ModelAdmin):
    fields = ['name', 'blog_image', 'description']



admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Blog, AdminBlog)