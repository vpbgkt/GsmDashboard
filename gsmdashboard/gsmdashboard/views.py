from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from Subjects.models import Subjects
from Video.models import Video


def aboutus(request):
    return render(request,'pages/aboutus.html', {'navbar': 'aboutus'})

def homepage(request):
    data = {
        'title' : 'home new'
    }
    return render(request,'index.html',data)


def subject(request):
    subjectData=Subjects.objects.all()
    subData = {
        'subjectData':subjectData
    } 
    # print(subData)
    return render(request, 'pages/subject.html',subData)



# def videos(request):
#     videoData=Video.objects.all()
#     Data = {
#         'videoData':videoData
#         }
#     return render(request, 'pages/videos.html',Data)



def subject_videos(request, subject_id):
    subject = get_object_or_404(Subjects, pk=subject_id)
    videos = Video.objects.filter(Subjects=subject)
    video_urls = [video.video_url for video in videos if video.video_url]  # fetch the video_url of each Video object
    context = {'subject': subject, 'videos': videos, 'video_urls': video_urls}
    print(context['video_urls'][0])
    
    return render(request, 'pages/subjectvideos.html', context)

