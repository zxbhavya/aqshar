# Generated by Django 4.2.11 on 2024-03-30 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0020_alter_donator_from_time_alter_donator_to_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="donator",
            name="from_time",
        ),
        migrations.RemoveField(
            model_name="donator",
            name="to_time",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="from_time",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="to_time",
        ),
    ]
