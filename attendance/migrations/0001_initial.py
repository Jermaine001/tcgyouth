# Generated by Django 5.1 on 2024-08-23 13:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('join_date', models.DateField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.member')),
            ],
            options={
                'unique_together': {('member', 'date')},
            },
        ),
    ]
