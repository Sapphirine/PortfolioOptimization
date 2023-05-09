# Generated by Django 4.1.2 on 2023-05-04 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockData",
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
                ("date", models.DateField()),
                ("low", models.FloatField()),
                ("open", models.FloatField()),
                ("volume", models.FloatField()),
                ("high", models.FloatField()),
                ("close", models.FloatField()),
                ("adjusted_close", models.FloatField()),
                ("stock", models.CharField(max_length=1)),
            ],
        ),
    ]
