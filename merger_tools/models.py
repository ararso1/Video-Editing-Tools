from django.db import models

from django.core.validators import FileExtensionValidator
from time import timezone
# Create your models here.

class Video(models.Model):

    original_video = models.FileField(upload_to='videos_uploaded',null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    merged_video = models.FileField(upload_to='videos_uploaded',null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)