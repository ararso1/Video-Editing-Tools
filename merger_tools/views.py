from django.shortcuts import render,redirect
from .form import *
from moviepy.editor import *
from django.core.files import File as DjangoFile
import os
import random
#from .videomerger import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        o_videos = request.FILES.getlist('original_video')
        m_videos = request.FILES.getlist('merged_video')
        scale = request.POST.get('scale')
            #clip1 = VideoFileClip(i.path)
            #durationc1=clip1.duration
            #print(durationc1)
            #clip2 = VideoFileClip(two)
            #durationc2=clip2.duration
        """ video_form= VideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            video_form.save()
            return redirect('templates') """

        for o_video in o_videos:
            o_vid = O_Video.objects.create(
                original_video=o_video,
            )
          
        for m_video in m_videos:
            m_vid = M_Video.objects.create(
                merged_video=m_video,
            )
        sc = Scale.objects.create(scale_type=scale)
                
          
        o_vid.save()
        m_vid.save()
        sc.save()
        return redirect('preview')

    context = {}
    return render(request, 'merger_tools/index.html', context)

def temp1(sound):
    cutted_o = Cut_Original.objects.all()
    cutted_m = Cut_Merged.objects.all()
    context = {}
    for i in cutted_o:
        o = i.cut_original.path 
        for j in cutted_m:
            m = j.cut_merged.path
            
            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            durationc1=clip1.duration
            print(durationc1)
            n=0
            durationc2=clip2.duration
            clips = [[clip1],[clip2]]
            if sound == 'no_sound':
                final1 = clips_array(clips).without_audio()
            elif sound == "s_from_original": 
                AudioClip=AudioFileClip("t1.mp4")
                final1 = clips_array(clips).set_audio(AudioClip)
            elif sound == "s_from_merged":
                AudioClip=AudioFileClip("t2.mp4")
                final1 = clips_array(clips).set_audio(AudioClip)
            else:
                final1 = clips_array(clips)
            final1.write_videofile("myfinal"+str(n)+".mp4", fps = 24, codec = 'mpeg4')

def temp2(sound):
    video = O_Video.objects.all()
    context = {'video':video}
    for i in video:
        print(i)
        for j in video:
            o = i.original_video.path 
            m = j.merged_video.path
        print("one",o)
        clip1 = VideoFileClip(m)
        durationc1=clip1.duration
        print(durationc1)
        clip2 = VideoFileClip(m)
        durationc2=clip2.duration
        clips = [[clip2],[clip1]]
        if sound == 'no_sound':
            final1 = clips_array(clips).without_audio()
        elif sound == "s_from_original": 
            AudioClip=AudioFileClip("t1.mp4")
            final1 = clips_array(clips).set_audio(AudioClip)
        elif sound == "s_from_merged":
            AudioClip=AudioFileClip("t2.mp4")
            final1 = clips_array(clips).set_audio(AudioClip)
        else:
            final1 = clips_array(clips)


def preview(request):
    o_video = O_Video.objects.all()
    m_video = M_Video.objects.all()
    
    listof_o=[]
    listof_m=[]
    for o in o_video:
        listof_o.append(o.original_video.path)
    for m in m_video:
        listof_m.append(m.merged_video.path)
    if request.method == "POST":
        #cut = request.POST.get('cut')
        video = request.POST.get('video')
        start = request.POST.get('start')
        end = request.POST.get('end')
      
        if start == '' and end == '':
            start=0
            end=0
        if video in listof_o:
            trim_original(start, end,video)
        else:
            trim_merged(start,end,video)

    context={'o_video':o_video, 'm_video':m_video}
    return render(request, 'merger_tools/preview.html', context)

def trim_original(start, end,video):
    
    num = random.randint(0,1000)
    clip1=VideoFileClip(video)
    clip1=clip1.cutout(start,end)
    print(clip1.duration)
    
    o = clip1.write_videofile(os.path.abspath("static/assets/cut_original/original"+str(num)+".mp4"), fps = 24, codec = 'mpeg4')
    #dir = os.path.abspath("original.mp4")
    #ile_obj1 = DjangoFile(open(clip1, mode='rb'), name=clip1)
    oo=Cut_Original.objects.create(cut_original=os.path.abspath("static/assets/cut_original/original"+str(num)+".mp4"))
    oo.save()
    #trimed_video = Cut_Original.objects.create(cut_original=final1)
    #trimed_video.save()
    


def trim_merged(start, end,video):
    num = random.randint(0,1000)
    clip1=VideoFileClip(video)
    clip1=clip1.cutout(start,end)
    print(clip1.duration)
    
    o = clip1.write_videofile(os.path.abspath("static/assets/cut_merged/merged"+str(num)+".mp4"), fps = 24, codec = 'mpeg4')
    #dir = os.path.abspath("original.mp4")
    #ile_obj1 = DjangoFile(open(clip1, mode='rb'), name=clip1)
    oo=Cut_Merged.objects.create(cut_merged=os.path.abspath("static/assets/cut_merged/merged"+str(num)+".mp4"))
    oo.save()
    #trimed_video = Cut_Original.objects.create(cut_original=final1)
    #trimed_video.save()

def templates(request):
    video = O_Video.objects.all()
    if request.method == 'POST':
        temp_name1 = request.POST.get('temp1')
        temp_name2 = request.POST.get('temp2')
        sound = request.POST.get('sound')
        cut = request.POST.get('cut')
        print(sound,cut)
        if temp_name1: 
            temp1(sound) 
        elif temp_name2:
            temp2(sound)
        return redirect('setting')

    context = {'video':video}
    return render(request, 'merger_tools/template.html', context)

def setting(request):
    return render(request, 'merger_tools/settings.html')

