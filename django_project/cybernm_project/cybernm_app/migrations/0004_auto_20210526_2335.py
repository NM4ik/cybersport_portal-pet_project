# Generated by Django 3.1.6 on 2021-05-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybernm_app', '0003_auto_20210526_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='limitation',
            field=models.CharField(choices=[('1', '1-5lvl'), ('2', '5-8'), ('3', '9-10')], max_length=20),
        ),
    ]
