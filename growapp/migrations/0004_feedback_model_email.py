# Generated by Django 5.1.4 on 2024-12-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growapp', '0003_complaints_model_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback_model',
            name='Email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]