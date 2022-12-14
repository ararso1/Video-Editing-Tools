from django.shortcuts import render,redirect
from .form import *
# Create your views here.

def index(request):
    video_form = VideoForm()
    if request.method == 'POST':
        video_form= VideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            video_form.save()
            return redirect('templates')
    context = {'video_fomr':video_form}
    return render(request, 'merger_tools/index.html', context)

def templates(request):
    context = {}
    return render(request, 'merger_tools/template.html', context)

def setting(request):
    return render(request, 'merger_tools/settings.html')