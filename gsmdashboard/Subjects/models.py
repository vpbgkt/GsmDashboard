from django.db import models
from django.contrib.auth.models import User

class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_description = models.TextField()
    Subject_image = models.ImageField(upload_to='subject_images/')

    def __str__(self):
        return self.subject_name
    