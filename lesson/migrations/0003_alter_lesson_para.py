# Generated by Django 4.2.20 on 2025-04-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_lesson_para'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='para',
            field=models.CharField(max_length=1),
        ),
    ]
