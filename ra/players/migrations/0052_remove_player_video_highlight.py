# Generated by Django 2.2.5 on 2020-01-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0051_auto_20200104_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='video_highlight',
        ),
    ]
