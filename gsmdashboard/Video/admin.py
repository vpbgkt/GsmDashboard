from django.contrib import admin
from Video.models import Video
class VideoAdmin(admin.ModelAdmin):
    list_display=('title','description','Subjects','video_file','thumbnail','video_url','uploaded_on')

admin.site.register(Video,VideoAdmin)




# Register your models here.
