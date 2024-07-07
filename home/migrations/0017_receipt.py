# Generated by Django 5.0.6 on 2024-07-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_delete_receipt"),
    ]

    operations = [
        migrations.CreateModel(
            name="Receipt",
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
                ("date", models.DateField(auto_now_add=True)),
                ("slno", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("admission_fee", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "personal_trainer_fee",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("multi_gym", models.BooleanField(default=False)),
                ("zumba", models.BooleanField(default=False)),
                ("yoga", models.BooleanField(default=False)),
                (
                    "gym_type_fee",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("in_words", models.CharField(max_length=1024)),
            ],
        ),
    ]
