# Generated by Django 3.2.9 on 2022-04-11 13:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='friend',
            field=models.ManyToManyField(blank=True, related_name='_accounts_customuser_friend_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
