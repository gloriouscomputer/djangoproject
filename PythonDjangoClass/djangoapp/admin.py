from django.contrib import admin

from .models import CustomUser, Blog, Student

class CustomUserAdmin(admin.ModelAdmin):
    fields = ['first_name','email', 'last_name','password', 'is_active', 'is_staff', 'is_superuser', 'user_role']

class AdminBlog(admin.ModelAdmin):
    fields = ['name', 'blog_image', 'description']



admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Blog, AdminBlog)