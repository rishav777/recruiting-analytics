# Generated by Django 2.2.5 on 2019-12-10 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0034_player_priority'),
        ('ra_user', '0012_watchlist'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='myboard',
            unique_together={('user', 'player')},
        ),
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('user', 'player')},
        ),
    ]
