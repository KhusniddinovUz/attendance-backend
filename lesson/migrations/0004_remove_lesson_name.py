# Generated by Django 4.2.20 on 2025-05-02 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_alter_lesson_para'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='name',
        ),
    ]
