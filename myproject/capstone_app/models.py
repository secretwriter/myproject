from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # link to Django User
    enrollment_date = models.DateField()
    role = models.CharField(
        max_length=10,
        choices=[('admin', 'Admin'), ('student', 'Student')],
        default='student'
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='games')
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
