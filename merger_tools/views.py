from django.shortcuts import render,redirect
from .form import *
from moviepy.editor import *
#from .videomerger import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        o_videos = request.FILES.getlist('original_video')
        m_videos = request.FILES.getlist('merged_video')
        """ video_form= VideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            video_form.save()
            return redirect('templates') """
        m=0
        for o_video in o_videos:
            video = Video.objects.create(
                original_video=o_video,
                merged_video=m_videos[m]
            )
            m+=1
        video.save()
        return redirect('templates')

    context = {}
    return render(request, 'merger_tools/index.html', context)

def temp1(request):
    o_video = Video.objects.all()
    for i in o_video:
        one = i.original_video 
        two = i.merged_video
    clip1 = VideoFileClip(one)
    durationc1=clip1.duration
    print(durationc1)
    clip2 = VideoFileClip(two)
    durationc2=clip2.duration
    #one = o_video[0]
    #two = o_video[1]


def templates(request):
    if request.method == 'POST':
        ori = request.POST.get('original')
        merg = request.POST.get('merged')
        print(ori,merg)
        return redirect('')

    context = {}
    return render(request, 'merger_tools/template.html', context)

def setting(request):
    return render(request, 'merger_tools/settings.html')