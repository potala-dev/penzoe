# Generated by Django 3.2 on 2021-05-22 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("books", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("modified", models.DateTimeField()),
                ("comments_count", models.IntegerField(default=0)),
                ("points", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Thread",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("body", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(editable=False)),
                ("modified", models.DateTimeField()),
                ("comments_count", models.IntegerField(default=0)),
                ("points", models.IntegerField(default=0)),
                ("hidden", models.BooleanField(default=False)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.book"
                    ),
                ),
            ],
        ),
    ]
