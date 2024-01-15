# Generated by Django 3.0.2 on 2023-11-29 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0073_disable_video_detection'),
    ]

    operations = [
        migrations.AddField(
            model_name='nefarioussettings',
            name='preferred_media_category',
            field=models.CharField(choices=[('movie', 'Movie'), ('tv', 'TV')], default='movie', max_length=10),
        ),
    ]