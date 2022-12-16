# Generated by Django 4.0.3 on 2022-12-16 08:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0002_rename_video_video_merged_video_video_original_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merged_video', models.FileField(null=True, upload_to='merged_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='O_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_video', models.FileField(null=True, upload_to='original_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
            ],
        ),
        migrations.DeleteModel(
            name='video',
        ),
    ]