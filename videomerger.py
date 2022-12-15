from moviepy.editor import *
 
# loading video dsa gfg intro video and getting only first 5 seconds
clip1 = VideoFileClip("t60.mp4")
durationc1=clip1.duration
clip2 = VideoFileClip("t2.mp4")
durationc2=clip2.duration

#for cutting the part of the video
def trim():
    starting = 5
    ending = 6
    clip_trim=clip1.cutout(starting,ending)

#for duration adjustment
if durationc1 <=durationc2:
    clip2 = VideoFileClip("t2.mp4").subclip(0, durationc1)
elif durationc1 >= durationc2:
    d=durationc1/durationc2
    d=int(d)
    print(d)
    l=[clip2]
    for i in range(d):
        l.append(clip2)
    clip2 =concatenate_videoclips(l).subclip(0, durationc1)

clips = [[clip1, clip2]]
sound=''

# for i in range(10):
#     for j in range(30):
#         pass


#for sound choice
if sound == 'No sound':
    final1 = clips_array(clips).without_audio()
elif sound == "Sound from original Video": 
   AudioClip=AudioFileClip("t1.mp4")
   final1 = clips_array(clips).set_audio(AudioClip)
elif sound == "Sound from merge Video":
   AudioClip=AudioFileClip("t2.mp4")
   final1 = clips_array(clips).set_audio(AudioClip)
else:
    final1 = clips_array(clips)
 # to make sound from the original videos 

# stacking clips
# final1.show()
final1.write_videofile("myfinal.mp4", fps = 24, codec = 'mpeg4')
 
# showing final clip
# final.ipython_display(width = 480)

#for up and bottom
# clips2 = [[clip1], [clip2]]
# final2 = clips_array(clips2)
# final2.write_videofile("myfinal2.mp4", fps = 24, codec = 'mpeg4')
