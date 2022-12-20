from django.shortcuts import render,redirect
from .form import *
from moviepy.editor import *
from moviepy.video.fx.all import *
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

        O_Video.objects.all().delete()
        M_Video.objects.all().delete()
        Cut_Original.objects.all().delete()
        Cut_Merged.objects.all().delete()
        Output_Video.objects.all().delete()

        for o_video in o_videos:
            o_vid = O_Video.objects.create(
                original_video=o_video,
            )
          
        for m_video in m_videos:
            m_vid = M_Video.objects.create(
                merged_video=m_video,
            )
                
        o_vid.save()
        m_vid.save()
        return redirect('preview')

    context = {}
    return render(request, 'merger_tools/index.html', context)


def temp1(sound,width,height,formats,crop_o,crop_m,resize):
    cutted_o = O_Video.objects.all()
    cutted_m = M_Video.objects.all()
    n=0

    for i in cutted_o:
        o = i.original_video.path 
        for j in cutted_m:
            m = j.merged_video.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)

            d1=clip1.duration
            d2=clip2.duration

            w1,h1=clip1.size
            w2,h2=clip2.size
            tobecut1 = h1-w1
            tobecut2 = h2-w2
            if crop_o == 'bottom' and crop_m == 'bottom':
                clip1 = vfx.crop(clip1, x1=0, y1=0, x2=w1, y2=w1)
                clip2 = vfx.crop(clip2, x1=0, y1=0, x2=w2, y2=w1)

            elif crop_o == 'top' and crop_m == 'bottom':
                clip1 = vfx.crop(clip1, x1=0, y1=tobecut1, x2=w1, y2=0)
                clip2 = vfx.crop(clip2, x1=0, y1=0, x2=w2, y2=w2)
                
            elif crop_o == 'bottom' and crop_m == 'top':
                clip1 = vfx.crop(clip1, x1=0, y1=0, x2=w1, y2=w1)
                clip2 = vfx.crop(clip2, x1=0, y1=tobecut2, x2=w2, y2=0)
                
            elif crop_o == 'middle' and crop_m == 'middle':
                pass
            
            elif crop_o == 'middle' and crop_m == 'top':
                pass

            elif crop_o == 'middle' and crop_m == 'bottom':
                pass

            else:
                clip1 = vfx.crop(clip1, x1=0, y1=tobecut1, x2=w1, y2=0)
                clip2 = vfx.crop(clip2, x1=0, y1=tobecut2, x2=w2, y2=0)
            
            """ if h1>=h2 and w1>=w2:
                clip2=clip2.fx(vfx.resize,(w1,h1))
            elif h1<h2 and w1<w2:
                clip1=clip1.fx(vfx.resize,(w2,h2))
            else:
                pass """

            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize)
            else:
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                select_sound(sound,o,m,n,clips,formats,resize)
            n+=1

def temp2(sound,width,height,formats):
    cutted_o = Cut_Original.objects.all()
    cutted_m = Cut_Merged.objects.all()
    n=0

    for i in cutted_o:
        o = i.cut_original.path 
        for j in cutted_m:
            m = j.cut_merged.path

            clip1 = VideoFileClip(o)
            clip2 = VideoFileClip(m)
            w1,h1=clip1.size
            w2,h2=clip2.size

            tobecut1 = h1-w1
            tobecut2 = h2-w2
            
            d1=clip1.duration
            d2=clip2.duration
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            else:
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            n+=1


def temp3(sound,width,height,formats):
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
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
        
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            else:
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            n+=1

def temp4(sound,width,height,formats):
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
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            else:
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            n+=1

def temp5(sound,width,height,formats):
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
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            else:
                clips = [[clip1],[clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            n+=1


def temp6(sound,width,height,formats):
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
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            else:
                clips = [[clip2],[clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            n+=1


def temp7(sound,width,height,formats):
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
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            else:
                clips = [[clip1,clip2]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            n+=1

def temp8(sound,width,height,formats):
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
            print('d1d2',d1,d2)
            if d2 > d1:
                clip2 = clip2.subclip(0, d1)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            elif d2 < d1:
                loop=d1/d2
                l=[clip2]
                for i in range(int(loop)):
                    l.append(clip2)
                clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            else:
                clips = [[clip2,clip1]]
                clips=clips_array(clips)
                clips.fx(vfx.resize,(width,height),width)
                select_sound(sound,o,m,n,clips,formats)
            n+=1


def select_sound(sound,o,m,n,clips,formats,resize):
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

    if resize == 'HD':
        final1=final1.fx(vfx.resize,(1080,1920))

    
    final1.write_videofile(os.path.abspath("static/assets/output_video/output"+str(n)+"."+formats), fps = 24, codec = 'mpeg4')
    oo=Output_Video.objects.create(output=os.path.abspath("static/assets/output_video/output"+str(n)+".mp4"))
    oo.save()
    """ elif formats == 'MOV':
        final1.write_videofile(os.path.abspath("static/assets/output_video/output"+str(n)+".MOV"), fps = 24, codec = 'mpeg4')
        oo=Output_Video.objects.create(output=os.path.abspath("static/assets/output_video/output"+str(n)+".MOV"))
        oo.save()
    elif formats == 'avi':
        final1.write_videofile(os.path.abspath("static/assets/output_video/output"+str(n)+".avi"), fps = 24, codec = 'mpeg4')
        oo=Output_Video.objects.create(output=os.path.abspath("static/assets/output_video/output"+str(n)+".avi"))
        oo.save()
    elif formats == 'webm':
        final1.write_videofile(os.path.abspath("static/assets/output_video/output"+str(n)+".webm"), fps = 24, codec = 'mpeg4')
        oo=Output_Video.objects.create(output=os.path.abspath("static/assets/output_video/output"+str(n)+".webm"))
        oo.save()
    else:
        final1.write_videofile(os.path.abspath("static/assets/output_video/output"+str(n)+".mkv"), fps = 24, codec = 'mpeg4')
        oo=Output_Video.objects.create(output=os.path.abspath("static/assets/output_video/output"+str(n)+".mkv"))
        oo.save() """


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

def dont_trim():
    print('wel.............')

def create_template(o_place,m_place,width,height,sound,formats):
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
                    select_sound(sound,o,m,n,clips,formats)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width)
                    select_sound(sound,o,m,n,clips,formats)
                else:
                    clips = [[clip1],[clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width)
                    select_sound(sound,o,m,n,clips,formats)

            elif o_place=='bottom' and m_place=='top':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)
                else:
                    clips = [[clip2],[clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)

            elif o_place=='left' and m_place=='right':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)
                else:
                    clips = [[clip1,clip2]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)

            elif o_place=='right' and m_place=='left':
                if d2 > d1:
                    clip2 = clip2.subclip(0, d1)
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)
                elif d2 < d1:
                    loop=d1/d2
                    l=[clip2]
                    for i in range(int(loop)):
                        l.append(clip2)
                    clip2 =concatenate_videoclips(l).subclip(0, clip1.duration)
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)
                else:
                    clips = [[clip2,clip1]]
                    clips=clips_array(clips)
                    clips=clips.fx(vfx.resize,(width,height),width= width)
                    select_sound(sound,o,m,n,clips,formats)
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
        dont_cut = request.POST.getlist('dont_cut')
        print(dont_cut)      
        if start == '' and end == '':
            start=0
            end=0
        if video in listof_o:
            trim_original(start, end,video)
        else:
            trim_merged(start,end,video)
    firsto=O_Video.objects.first().id
    lasto=O_Video.objects.last().id
    firstm=M_Video.objects.first().id
    lastm=M_Video.objects.last().id
    context={'o_video':o_video, 'm_video':m_video,'firstm':firstm,'lastm':lastm,'firsto':firsto,'lasto':lasto}
    return render(request, 'merger_tools/preview.html', context)


def templates(request):
    #video = O_Video.objects.all()
    error = ''
    if request.method == 'POST':
        temp_name1 = request.POST.get('temp1')
        temp_name2 = request.POST.get('temp2')
        temp_name3 = request.POST.get('temp3')
        temp_name4 = request.POST.get('temp4')
        temp_name5 = request.POST.get('temp5')
        temp_name6 = request.POST.get('temp6')
        temp_name7 = request.POST.get('temp7')
        temp_name8 = request.POST.get('temp8')

        formats = request.POST.get('format')
        
        crop_o = request.POST.get('crop_original')
        crop_m = request.POST.get('crop_merged')
        resize = request.POST.get('resize')

        o_place = request.POST.get('o_place')
        m_place = request.POST.get('m_place')
        width = request.POST.get('width')
        height = request.POST.get('height')
        sound = request.POST.get('sound')
        
        if o_place!=None and m_place!=None and width!=None and height!=None:
            create_template(o_place,m_place,width,height,sound,formats,resize)
        elif temp_name1:
            width=720
            height=1280 
            temp1(sound,width,height,formats, crop_o,crop_m,resize)
        elif temp_name2:
            width=720
            height=1280 
            temp2(sound,width,height,formats) 
        elif temp_name3:
            width=720
            height=1280 
            temp3(sound,width,height,formats) 
        elif temp_name4:
            width=720
            height=1280 
            temp4(sound,width,height,formats)  
        elif temp_name5:
            width=720
            height=720 
            temp5(sound,width,height,formats)  
        elif temp_name6:
            width=720
            height=720
            temp6(sound,width,height,formats)  
        elif temp_name7:
            width=720
            height=720 
            temp7(sound,width,height,formats)  
        elif temp_name8:
            width=720
            height=720 
            temp8(sound,width,height,formats) 
        else:
            error = 'Please select the correct template'
        return redirect('output')

    context = {'error':error}
    return render(request, 'merger_tools/template.html', context)

def output(request):
    outputs = Output_Video.objects.all()
    context = {'outputs':outputs}
    return render(request, 'merger_tools/output.html', context)

def scrap_video():
    s = Service('C:\Program Files (x86)\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # You may use headless if you choose
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-dev-shm-usage")

    proxy_address = os.environ.get("HTTP_PROXY")

    if proxy_address:
        options.add_argument(f"--proxy-server={proxy_address}")
    driver = webdriver.Chrome(service=s, options=options)
    URL = 'http://127.0.0.1:8000/output'
    driver.get(URL)
    donwload = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/a')
    for i in donwload:
        print(i.text)
    print(1)



def DonCut(request,oi,of,mi,mf):
    firsto=int(oi)
    lasto=int(of)
    firstm=int(mi)
    lastm=int(mf)
    o_video = O_Video.objects.all()
    m_video = M_Video.objects.all()
    
    """     if video in listof_o:
        trim_original(start, end,video)
    else:
        trim_merged(start,end,video) """
    o=0
    for i in range(firsto,lasto+1):
        print(o_video[o].id==i)
        dont_trim()
        o+=1
    m=0
    for j in range(firstm,lastm+1):
        print(m_video[m].id==j)
        
    return redirect('templates')















