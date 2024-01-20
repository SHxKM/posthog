# Generated by Django 3.2.19 on 2023-10-13 09:13

import django.db.models.deletion
from django.db import migrations, models

import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0354_organization_never_drop_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batchexportdestination",
            name="type",
            field=models.CharField(
                choices=[
                    ("S3", "S3"),
                    ("Snowflake", "Snowflake"),
                    ("Postgres", "Postgres"),
                    ("BigQuery", "Bigquery"),
                    ("NoOp", "Noop"),
                ],
                help_text="A choice of supported BatchExportDestination types.",
                max_length=64,
            ),
        ),
        migrations.CreateModel(
            name="BatchExportBackfill",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "start_at",
                    models.DateTimeField(help_text="The start of the data interval."),
                ),
                (
                    "end_at",
                    models.DateTimeField(help_text="The end of the data interval."),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Cancelled", "Cancelled"),
                            ("Completed", "Completed"),
                            ("ContinuedAsNew", "Continuedasnew"),
                            ("Failed", "Failed"),
                            ("Terminated", "Terminated"),
                            ("TimedOut", "Timedout"),
                            ("Running", "Running"),
                            ("Starting", "Starting"),
                        ],
                        help_text="The status of this backfill.",
                        max_length=64,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The timestamp at which this BatchExportBackfill was created.",
                    ),
                ),
                (
                    "finished_at",
                    models.DateTimeField(
                        help_text="The timestamp at which this BatchExportBackfill finished, successfully or not.",
                        null=True,
                    ),
                ),
                (
                    "last_updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The timestamp at which this BatchExportBackfill was last updated.",
                    ),
                ),
                (
                    "batch_export",
                    models.ForeignKey(
                        help_text="The BatchExport this backfill belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.batchexport",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        help_text="The team this belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.team",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
