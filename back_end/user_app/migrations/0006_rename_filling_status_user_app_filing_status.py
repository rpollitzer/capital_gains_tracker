# Generated by Django 4.2.4 on 2023-09-04 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_rename_estamated_year_income_user_app_estimated_year_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_app',
            old_name='filling_status',
            new_name='filing_status',
        ),
    ]
