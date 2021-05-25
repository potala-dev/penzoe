# Generated by Django 3.2 on 2021-05-25 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('comments_count', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('hidden', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('modified', models.DateTimeField()),
                ('comments_count', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discourse.thread')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
