# Generated by Django 5.0.2 on 2024-02-16 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_remove_mobilelegends_final'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datashark',
            name='final',
        ),
    ]
