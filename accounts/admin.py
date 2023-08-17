from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Custom


class UserAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'username', 'email', 'is_active', 'is_customuser', 'is_staff']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff']

    class Meta:
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class ScoreAdmin(admin.ModelAdmin):
#     list_display = [
#         'student', 'course', 'assignment', 'mid_exam', 'quiz',
#         'attendance', 'final_exam', 'total', 'grade', 'comment'
#     ]


admin.site.register(User, UserAdmin)
admin.site.register(Custom)

# admin.site.unregister(Group)
