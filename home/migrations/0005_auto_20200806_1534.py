# Generated by Django 2.2.15 on 2020-08-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_auto_20200806_1529"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customtext", old_name="first_name", new_name="first_update",
        ),
        migrations.RenameField(
            model_name="customtext", old_name="last_name", new_name="last_update",
        ),
        migrations.RenameField(
            model_name="customtext", old_name="address", new_name="new_address",
        ),
        migrations.RemoveField(model_name="customtext", name="title",),
        migrations.AddField(
            model_name="customtext",
            name="title_update",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
