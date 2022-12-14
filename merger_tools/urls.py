
from . import views
from django.urls import path


urlpatterns = [
    
    path("", views.index, name = 'index'),
    path('templates', views.templates, name='templates'),
    path('setting', views.setting, name='setting'),
]
