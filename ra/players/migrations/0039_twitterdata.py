# Generated by Django 2.2.5 on 2019-12-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0038_player_nfl_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
