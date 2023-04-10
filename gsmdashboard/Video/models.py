from django.db import models
from Subjects.models import Subjects

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    Subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/',null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',null=True,blank=True)
    video_url = models.URLField(null=True,blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title