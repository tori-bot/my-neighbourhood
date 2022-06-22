# Generated by Django 4.0.5 on 2022-06-22 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood_app', '0024_profile_hood_alter_neighborhood_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='user',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='occupants',
            field=models.IntegerField(default=0),
        ),
    ]