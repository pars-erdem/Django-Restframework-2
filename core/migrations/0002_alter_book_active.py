# Generated by Django 5.0.6 on 2024-07-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active book'),
        ),
    ]
