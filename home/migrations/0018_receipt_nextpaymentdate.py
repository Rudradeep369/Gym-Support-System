# Generated by Django 5.0.6 on 2024-07-07 18:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0017_receipt"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="nextPaymentDate",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
