from django.http import HttpResponse
from django.shortcuts import render, redirect ,get_object_or_404
from Subjects.models import Subjects
from Video.models import Video
from Eclass.models import Eclass
from accounts.models import UserProfile
from django.contrib import messages 


from django.contrib.auth.models import User


def aboutus(request):
    return render(request, 'pages/aboutus.html', {'navbar': 'aboutus'})


def homepage(request):
    data = {
        'title': 'home new'
    }
    return render(request, 'index.html', data)


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

    return render(request, 'pages/classeslist.html', context)


def subject_videos(request, subject_id):
    subject = get_object_or_404(Subjects, pk=subject_id)
    videos = Video.objects.filter(Subjects=subject)
    # fetch the video_url of each Video object
    video_urls = [video.video_url for video in videos if video.video_url]
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
    return render(request, 'pages/contect.html')


def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        # Check if passwords match
        if password != confirmpassword:
            pass
            # Add appropriate error handling or validation

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

         # Create a user profile
        profile = UserProfile(user=user)
        profile.save()

        messages.success(request,"You are registred sucessfully")

        # Redirect to a success page or desired URL
        # return redirect('success-page')

    return render(request, '/')
