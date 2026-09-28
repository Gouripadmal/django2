from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    id_card = models.FileField()

    def __str__(self):
        return self.full_name