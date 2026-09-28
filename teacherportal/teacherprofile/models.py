from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    profile_photo = models.FileField()

    def __str__(self):
        return self.first_name + " " + self.last_name