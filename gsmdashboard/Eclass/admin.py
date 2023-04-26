from django.contrib import admin
from .models import Eclass
class EclassAdmin(admin.ModelAdmin):
    list_display=('name','description')

admin.site.register(Eclass, EclassAdmin)
