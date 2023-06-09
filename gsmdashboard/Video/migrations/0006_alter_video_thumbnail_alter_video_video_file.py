# Generated by Django 4.1.7 on 2023-04-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0005_alter_video_thumbnail_alter_video_video_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/videos/'),
        ),
    ]
