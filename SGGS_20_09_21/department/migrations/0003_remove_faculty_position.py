# Generated by Django 5.1.4 on 2025-02-13 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_alter_students_noofstudents_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='position',
        ),
    ]
