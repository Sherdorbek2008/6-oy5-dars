from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name