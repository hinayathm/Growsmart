# Generated by Django 5.1.4 on 2024-12-19 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growapp', '0005_feedback_model_created_at_feedback_model_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback_model',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='feedback_model',
            name='updated_at',
        ),
    ]
