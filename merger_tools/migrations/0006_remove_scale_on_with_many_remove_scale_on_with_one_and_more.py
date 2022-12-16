# Generated by Django 4.0.3 on 2022-12-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0005_rename_on_by_many_scale_on_with_many_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scale',
            name='on_with_many',
        ),
        migrations.RemoveField(
            model_name='scale',
            name='on_with_one',
        ),
        migrations.AddField(
            model_name='scale',
            name='scale_type',
            field=models.CharField(choices=[('one_with_one', 'One with one'), ('one_with_many', 'One with many')], max_length=20, null=True),
        ),
    ]