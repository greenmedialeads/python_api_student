from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    student_image = models.ImageField(upload_to='student_images/')

    def __str__(self):
        return self.name
