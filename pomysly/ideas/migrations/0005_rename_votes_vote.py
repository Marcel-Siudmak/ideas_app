# Generated by Django 4.0.1 on 2022-06-09 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_alter_idea_youtube'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
