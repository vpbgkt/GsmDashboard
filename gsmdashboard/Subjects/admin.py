from django.contrib import admin
from Subjects.models import Subjects
class SubjectsAdmin(admin.ModelAdmin):
    list_display=('subject_name','subject_description','Subject_image' )

admin.site.register(Subjects,SubjectsAdmin)

# Register your models here.
