from moviepy.editor import *
from .views import * 
from .models import *
from moviepy.video.fx.all import *

clip1 = VideoFileClip('C:\Users\Csolve\Videos\Captures\original.mp4')
clip2 = VideoFileClip('C:\Users\Csolve\Videos\Captures\merged.mp4')

w1,h1=clip1.size
w2,h2=clip2.size

tobecut1 = h1-w1
tobecut2 = h2-w2

clip1.fx(vfx.resize,(w1,1),w1)

clip1.write_videofile("new1.mp4", fps = 24, codec = 'mpeg4')
