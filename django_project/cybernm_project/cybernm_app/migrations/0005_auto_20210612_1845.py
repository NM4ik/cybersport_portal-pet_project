# Generated by Django 3.1.6 on 2021-06-12 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybernm_app', '0004_auto_20210612_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(related_name='tournament_player', to=settings.AUTH_USER_MODEL, verbose_name='игроки'),
        ),
    ]