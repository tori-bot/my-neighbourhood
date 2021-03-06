# Generated by Django 4.0.5 on 2022-06-20 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood_app', '0011_alter_business_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbors', to='neighbourhood_app.neighborhood'),
        ),
    ]
