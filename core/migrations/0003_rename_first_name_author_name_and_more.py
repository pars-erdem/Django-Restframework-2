# Generated by Django 5.0.6 on 2024-07-07 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_book_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
    ]