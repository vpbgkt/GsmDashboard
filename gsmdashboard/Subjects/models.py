from django.db import models
from Eclass.models import Eclass


class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_description = models.TextField()
    Subject_image = models.ImageField(upload_to='uploads/subject_images/')
    eclass = models.ForeignKey(Eclass, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.subject_name
