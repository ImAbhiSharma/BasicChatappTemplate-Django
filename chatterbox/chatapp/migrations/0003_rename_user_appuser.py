# Generated by Django 4.1.5 on 2023-01-29 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_user_last_seen_user_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AppUser',
        ),
    ]
