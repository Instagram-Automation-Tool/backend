# Generated by Django 4.1.1 on 2022-11-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Follower",
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
                ("fullName", models.CharField(max_length=65)),
                ("isVerified", models.BooleanField()),
                ("profilePictureURL", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="InstagramAccount",
            fields=[
                ("expandiId", models.CharField(max_length=100)),
                (
                    "username",
                    models.CharField(max_length=31, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=120)),
                ("cookies", models.JSONField()),
                ("proxy", models.CharField(max_length=100)),
                ("bio", models.CharField(max_length=151)),
                ("followerCount", models.IntegerField()),
                ("followingCount", models.IntegerField(default=-1)),
                ("postsCount", models.IntegerField(default=-1)),
                ("profilePictureURL", models.CharField(max_length=100000)),
            ],
        ),
    ]
