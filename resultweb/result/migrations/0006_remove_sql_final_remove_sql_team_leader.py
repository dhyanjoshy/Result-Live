# Generated by Django 5.0.2 on 2024-02-16 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_remove_datashark_final'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sql',
            name='final',
        ),
        migrations.RemoveField(
            model_name='sql',
            name='team_leader',
        ),
    ]
