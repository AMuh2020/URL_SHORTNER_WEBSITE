# Generated by Django 4.2.4 on 2023-08-24 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('url_redirect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]