from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from Subjects.models import Subjects
from Video.models import Video
from Eclass.models import Eclass


def aboutus(request):
    return render(request,'pages/aboutus.html', {'navbar': 'aboutus'})

def homepage(request):
    data = {
        'title' : 'home new'
    }
    return render(request,'index.html',data)


# def subject(request):
#     subjectData=Subjects.objects.all()
#     subData = {
#         'subjectData':subjectData
#     } 
#     # print(subData)
#     return render(request, 'pages/subject.html',subData)



# def videos(request):
#     videoData=Video.objects.all()
#     Data = {
#         'videoData':videoData
#         }
#     return render(request, 'pages/videos.html',Data)

def eclass_list(request):
    eclasses = Eclass.objects.all()
    context = {'eclasses': eclasses}
    
    return render(request, 'pages/eclass_list.html', context)


def subject_videos(request, subject_id):
    subject = get_object_or_404(Subjects, pk=subject_id)
    videos = Video.objects.filter(Subjects=subject)
    video_urls = [video.video_url for video in videos if video.video_url]  # fetch the video_url of each Video object
    context = {'subject': subject, 'videos': videos, 'video_urls': video_urls}
    
    return render(request, 'pages/subjectvideos.html', context)

def subject(request, class_name):
    eclass = get_object_or_404(Eclass, name=class_name)
    if subjects := Subjects.objects.filter(eclass=eclass):
        context = {'eclass': eclass, 'subjects': subjects}
        return render(request, 'pages/subjects.html', context)
    else:
        context = {'eclass': eclass}
        return render(request, 'pages/no_subjects.html', context)
    

def contect(request):
    return render(request,'pages/contect.html')