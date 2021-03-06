# Generated by Django 3.1.2 on 2022-04-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20220415_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_question',
            name='difficulty_level',
            field=models.CharField(blank=b'I00\n', choices=[('B', 'BASIC'), ('I', 'INTERMEDIAT'), ('A', 'ADVANCED'), ('E', 'EXPERT')], default='B', help_text='Level of Dificulty to be juged by the author', max_length=1),
        ),
    ]
