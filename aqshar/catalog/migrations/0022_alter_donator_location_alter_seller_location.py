# Generated by Django 4.2.11 on 2024-03-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0021_remove_donator_from_time_remove_donator_to_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donator",
            name="location",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="seller",
            name="location",
            field=models.TextField(blank=True, null=True),
        ),
    ]