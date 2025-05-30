# Generated by Django 5.1.4 on 2025-02-13 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('departmentid', models.AutoField(primary_key=True, serialize=False)),
                ('departmentname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyname', models.CharField(max_length=100)),
                ('facultyemail', models.EmailField(max_length=100)),
                ('position', models.CharField(max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
                ('noofsubjects', models.PositiveIntegerField(max_length=10)),
                ('noofstudents', models.PositiveIntegerField(max_length=80)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.faculty')),
            ],
        ),
    ]
