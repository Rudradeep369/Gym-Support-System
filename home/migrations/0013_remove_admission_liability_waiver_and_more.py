# Generated by Django 5.0.6 on 2024-07-04 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_admission_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admission",
            name="liability_waiver",
        ),
        migrations.RemoveField(
            model_name="admission",
            name="marketing_consent",
        ),
        migrations.RemoveField(
            model_name="admission",
            name="privacy_policy",
        ),
        migrations.RemoveField(
            model_name="admission",
            name="terms_conditions",
        ),
    ]
