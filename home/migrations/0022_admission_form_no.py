# Generated by Django 5.0.6 on 2024-07-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0021_remove_receipt_id_alter_receipt_admission_fee_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission",
            name="form_no",
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
