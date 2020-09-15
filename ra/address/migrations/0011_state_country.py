# Generated by Django 2.2.5 on 2019-12-28 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0010_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.Country'),
        ),
    ]
