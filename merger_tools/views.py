from django.shortcuts import render,redirect
from .form import *
# Create your views here.

def index(request):
    video_form = VideoForm()
    if request.method == 'POST':
        video_form= VideoForm(request.POST, request.FILES)
        #o_video = request.POST.get('original_video')
        #m_video = request.POST.get('merged_video')
        if video_form.is_valid():
            video_form.save()
            return redirect('templates')
    context = {'video_fomr':video_form}
    return render(request, 'merger_tools/index.html', context)