# Generated by Django 2.1.1 on 2018-11-20 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20181120_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
