# Generated by Django 4.0.5 on 2022-06-22 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood_app', '0023_alter_posts_neighborhood_alter_posts_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood_app.neighborhood'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood_app.profile'),
        ),
    ]
