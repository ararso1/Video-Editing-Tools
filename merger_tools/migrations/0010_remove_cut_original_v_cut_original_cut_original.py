# Generated by Django 4.0.3 on 2022-12-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0009_remove_cut_original_cut_original_cut_original_v'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cut_original',
            name='v',
        ),
        migrations.AddField(
            model_name='cut_original',
            name='cut_original',
            field=models.FileField(null=True, upload_to='cut_original'),
        ),
    ]