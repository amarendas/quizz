# Generated by Django 3.2.5 on 2022-04-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20220429_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_question',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]