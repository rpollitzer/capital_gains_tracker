# Generated by Django 4.2.4 on 2023-08-15 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_alter_user_app_estamated_year_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_app',
            old_name='estamated_year_income',
            new_name='estimated_year_income',
        ),
    ]
