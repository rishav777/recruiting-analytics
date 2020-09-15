# Generated by Django 2.2.5 on 2019-10-17 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_school'),
        ('ra_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.Address')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.School')),
            ],
        ),
    ]
