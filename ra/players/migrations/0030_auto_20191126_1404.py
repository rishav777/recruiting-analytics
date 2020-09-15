# Generated by Django 2.2.5 on 2019-11-26 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0029_auto_20191120_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedsearch',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='savedsearch',
            unique_together={('name', 'search_by')},
        ),
    ]
