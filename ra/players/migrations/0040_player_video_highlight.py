# Generated by Django 2.2.5 on 2019-12-19 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0039_twitterdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='video_highlight',
            field=models.FileField(blank=True, null=True, upload_to='highlighted-videos/'),
        ),
    ]
