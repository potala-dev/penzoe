# Generated by Django 3.2 on 2021-05-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20210530_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='repetitions',
            field=models.IntegerField(null=True, verbose_name='Repetitions'),
        ),
    ]
