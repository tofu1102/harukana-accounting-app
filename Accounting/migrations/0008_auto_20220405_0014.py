# Generated by Django 3.2.9 on 2022-04-04 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounting', '0007_alter_pay_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Member',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pay',
            name='payee',
            field=models.ManyToManyField(related_name='payee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pay',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='member',
        ),
    ]