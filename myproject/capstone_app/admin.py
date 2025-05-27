from django.contrib import admin
from .models import Student, Game

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def name(self, obj):
        return obj.user.get_full_name() or obj.user.username

    def email(self, obj):
        return obj.user.email

    list_display = ['name', 'email', 'role', 'enrollment_date']
    search_fields = ['user__username', 'user__email', 'role']
