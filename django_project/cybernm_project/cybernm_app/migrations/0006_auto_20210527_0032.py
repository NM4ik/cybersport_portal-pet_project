# Generated by Django 3.1.6 on 2021-05-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybernm_app', '0005_auto_20210526_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='limitation',
            field=models.CharField(choices=[('f15', '1-5lvl'), ('f58', '5-8lvl'), ('f810', '8-10lvl')], max_length=20),
        ),
    ]
