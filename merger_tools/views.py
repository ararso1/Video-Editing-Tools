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
    n=0
    for i in cutted_o:
        o = i.cut_original.path 
        for j in cutted_m:
            m = j.cut_merged.path
            
            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)

            d1=clip1.duration
            d2=clip2.duration
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1],[clip2]]
                select_sound(sound,o,m,n,clips)
            elif d2 < d1:
                loop=d1/d2
                print('ddddddddddddddddddddddd',loop,int(loop))
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1],[clip2]]
                select_sound(sound,o,m,n,clips)
            else:
                clips = [[clip1],[clip2]]
                select_sound(sound,o,m,n,clips)
            n+=1

def fetch_video():
    cutted_o = Cut_Original.objects.all()
    cutted_m = Cut_Merged.objects.all()
    context = {}
    for i in cutted_o:
        o = i.cut_original.path 
        for j in cutted_m:
            m = j.cut_merged.path
            
            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)


def temp2(sound):
    cutted_o = Cut_Original.objects.all()
    cutted_m = Cut_Merged.objects.all()
    n=0
    for i in cutted_o:
        o = i.cut_original.path 
        for j in cutted_m:
            m = j.cut_merged.path
            
            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            clips = [[clip2], [clip1]]
            select_sound(sound,o,m,n,clips)
            n+=0

def select_sound(sound,o,m,n,clips):
    if sound == 'no_sound':
        final1 = clips.without_audio()
    elif sound == "s_from_original": 
        AudioClip=AudioFileClip(o)
        final1 = clips.set_audio(AudioClip)
    elif sound == "s_from_merged":
        AudioClip=AudioFileClip(m)
        final1 = clips.set_audio(AudioClip)
    else:
        final1 = clips
    
    final1.write_videofile(os.path.abspath("static/assets/output_video/output"+str(n)+".mp4"), fps = 24, codec = 'mpeg4')
    oo=Output_Video.objects.create(output=os.path.abspath("static/assets/output_video/output"+str(n)+".mp4"))
    oo.save()


def trim_original(start, end,video):
    
    num = random.randint(0,1000)
    clip1=VideoFileClip(video)
    clip1=clip1.cutout(start,end)
    
    clip1.write_videofile(os.path.abspath("static/assets/cut_original/original"+str(num)+".mp4"), fps = 24, codec = 'mpeg4')
    oo=Cut_Original.objects.create(cut_original=os.path.abspath("static/assets/cut_original/original"+str(num)+".mp4"))
    oo.save()

    
def trim_merged(start, end,video):
    num = random.randint(0,1000)
    clip1=VideoFileClip(video)
    clip1=clip1.cutout(start,end)
    print(clip1.duration)
    
    o = clip1.write_videofile(os.path.abspath("static/assets/cut_merged/merged"+str(num)+".mp4"), fps = 24, codec = 'mpeg4')
    oo=Cut_Merged.objects.create(cut_merged=os.path.abspath("static/assets/cut_merged/merged"+str(num)+".mp4"))
    oo.save()

def create_template(o_place,m_place,width,height,sound):
    cutted_o = Cut_Original.objects.all()
    cutted_m = Cut_Merged.objects.all()
    n=0
    for i in cutted_o:
        o = i.cut_original.path 
        for j in cutted_m:
            m = j.cut_merged.path
            
            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            d1=clip1.duration
            d2=clip2.duration
            if o_place=='top' and m_place=='bottom':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width)
                    select_sound(sound,o,m,n,clips)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width)
                    select_sound(sound,o,m,n,clips)
                else:
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width)
                    select_sound(sound,o,m,n,clips)

            elif o_place=='bottom' and m_place=='top':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)
                else:
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)

            elif o_place=='left' and m_place=='right':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)
                else:
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)

            elif o_place=='right' and m_place=='left':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)
                else:
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips)
            else:
                print('The selected merging is not correct!!!!!!!!!')                

            n+=1


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


def templates(request):
    #video = O_Video.objects.all()
    if request.method == 'POST':
        temp_name1 = request.POST.get('temp1')
        temp_name2 = request.POST.get('temp2')
        o_place = request.POST.get('o_place')
        m_place = request.POST.get('m_place')
        width = request.POST.get('width')
        height = request.POST.get('height')
        sound = request.POST.get('sound')

        if o_place!=None and m_place!=None and width!=None and height!=None:
            create_template(o_place,m_place,width,height,sound)
        elif temp_name1: 
            temp1(sound) 
        elif temp_name2:
            temp2(sound)
        else:
            print('Please select the correct template')
        return redirect('output')

    #context = {'video':video}
    return render(request, 'merger_tools/template.html')

def output(request):
    outputs = Output_Video.objects.all()
    context = {'outputs':outputs}
    return render(request, 'merger_tools/output.html', context)

def temp(request):
    outputs = Output_Video.objects.all()
    context = {'outputs':outputs}
    return render(request, 'merger_tools/temp1.html', context)

