# Generated by Django 2.2.5 on 2019-10-18 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_school'),
        ('players', '0005_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.City'),
        ),
        migrations.AddField(
            model_name='player',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.Classification'),
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ManyToManyField(related_name='player_positions', to='players.Positions'),
        ),
        migrations.AddField(
            model_name='player',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.PlayerType'),
        ),
        migrations.AddField(
            model_name='player',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.School'),
        ),
        migrations.AddField(
            model_name='player',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.State'),
        ),
    ]
