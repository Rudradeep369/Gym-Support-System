# Generated by Django 5.0.6 on 2024-06-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_admission_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission",
            name="profile_image",
            field=models.ImageField(
                default="https://www.w3schools.com/howto/img_avatar.png",
                upload_to="images/",
            ),
        ),
    ]
