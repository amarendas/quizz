# Generated by Django 3.1.2 on 2022-04-02 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20220402_1708'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quiz',
            new_name='Quiz_Question',
        ),
    ]
