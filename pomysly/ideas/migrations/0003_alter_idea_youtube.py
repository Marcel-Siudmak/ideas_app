# Generated by Django 4.0.1 on 2022-06-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_votes_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='youtube',
            field=models.URLField(null=True),
        ),
    ]
