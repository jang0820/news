# Generated by Django 4.2 on 2024-07-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="news title", max_length=100, verbose_name="title"
                    ),
                ),
                (
                    "content",
                    models.TextField(help_text="news content", verbose_name="content"),
                ),
                ("createtime", models.DateTimeField(auto_now=True)),
                ("count", models.IntegerField()),
                ("file", models.FileField(upload_to="upload/")),
            ],
        ),
    ]
