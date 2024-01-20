# Generated by Django 3.2.19 on 2023-11-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0368_externaldatasource_prefix"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="theme_mode",
            field=models.CharField(
                blank=True, choices=[("light", "Light"), ("dark", "Dark")], max_length=20, null=True
            ),
        ),
    ]
