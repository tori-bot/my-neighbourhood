# Generated by Django 4.0.5 on 2022-06-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood_app', '0003_profile_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.EmailField(max_length=300),
        ),
    ]