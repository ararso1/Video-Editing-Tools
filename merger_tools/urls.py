
from . import views
from django.urls import path


urlpatterns = [
    
    path("", views.index, name = 'index'),
    path('preview', views.preview, name='preview'),
    path('templates', views.templates, name='templates'),
    path('setting', views.setting, name='setting'),
    path('temp1', views.temp1, name='temp1'),
]
