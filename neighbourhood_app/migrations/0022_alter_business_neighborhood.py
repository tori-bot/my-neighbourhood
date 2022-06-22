# Generated by Django 4.0.5 on 2022-06-21 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood_app', '0021_alter_business_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood_app.neighborhood'),
        ),
    ]
