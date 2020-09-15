# Generated by Django 2.2.5 on 2019-11-15 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_school_logo'),
        ('players', '0023_fbshardcommit'),
    ]

    operations = [
        migrations.CreateModel(
            name='FbsOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(blank=True, max_length=5, null=True)),
                ('hard_commit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.FbsHardCommit')),
                ('schools', models.ManyToManyField(blank=True, null=True, related_name='fbs_offers', to='address.School')),
                ('visits', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.SchoolsVisit')),
            ],
        ),
    ]
