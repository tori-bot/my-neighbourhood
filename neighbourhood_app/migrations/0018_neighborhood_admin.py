# Generated by Django 4.0.5 on 2022-06-21 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood_app', '0017_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood_app.profile'),
        ),
    ]
