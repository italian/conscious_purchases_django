# Generated by Django 4.2.11 on 2024-04-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="result",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
