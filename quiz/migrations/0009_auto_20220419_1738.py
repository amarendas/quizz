# Generated by Django 3.1.2 on 2022-04-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20220419_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_question',
            name='answer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quiz_question',
            name='extra',
            field=models.TextField(help_text='Some extra interesting  info on the answer', max_length=500, null=True),
        ),
    ]
