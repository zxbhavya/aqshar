# Generated by Django 4.2.11 on 2024-03-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0019_donator_from_time_donator_to_time_seller_from_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donator",
            name="from_time",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="donator",
            name="to_time",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="seller",
            name="from_time",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="seller",
            name="to_time",
            field=models.TimeField(),
        ),
    ]