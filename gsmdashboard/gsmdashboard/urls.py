"""gsmdashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views ome
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))import H
"""
from django.contrib import admin
from django.urls import path
from gsmdashboard import settings, views
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('subject/', views.subject, name='subject'),
    path('eclass_list/', views.eclass_list, name='eclass_list'),
    path('subject/<subject_id>/', views.subject_videos, name='subject_videos'),
    # path('eclass_list/<int:eclass_id>/', name='subjects'),
    path('eclass_list/<str:class_name>/',views.subject, name='eclass_list'),
    path('contect/', views.contect, name='contect'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # New
