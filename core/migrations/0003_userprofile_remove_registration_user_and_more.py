# Generated by Django 5.1 on 2024-10-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_attendance_registration_delete_myuser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('age', models.PositiveIntegerField(editable=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=10)),
                ('residence', models.CharField(max_length=100)),
                ('date_joined', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
