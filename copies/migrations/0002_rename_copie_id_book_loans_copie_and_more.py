# Generated by Django 4.2.1 on 2023-05-03 19:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book_loans",
            old_name="copie_id",
            new_name="copie",
        ),
        migrations.RenameField(
            model_name="book_loans",
            old_name="user_id",
            new_name="user",
        ),
    ]
