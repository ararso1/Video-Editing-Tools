from moviepy.editor import *

from moviepy.video.fx.all import *

clip1 = VideoFileClip('original.mp4')
clip2 = VideoFileClip('merged.mp4')

w1,h1=clip1.size
w2,h2=clip2.size

tobecut1 = h1-w1
tobecut2 = h2-w2
print(tobecut1)
#clip1=clip1.fx(vfx.resize,(w1,w1))
clip2=clip2.fx(vfx.resize,(w2,w2))
print(clip2.size)
clip=[[clip1],[clip2]]
clip=clips_array(clip)
clip1 = vfx.crop(clip1, x1=0, y1=0, x2=576, y2=576)
#after joined
if h1>=h2 and w1>=w2:
    clip=clip.fx(vfx.resize,(w1,h1))
elif h1<h2 and w1<w2:
    clip=clip.fx(vfx.resize,(w2,h2))
else:
    clip=clip.fx(vfx.resize,(w2,h2))


print(clip1.size)
clip1=clip1.fx(vfx.resize,(1080,1920))
print(clip1.size)
clip1.write_videofile("new1.mp4", fps = 30, codec = 'mpeg4')
