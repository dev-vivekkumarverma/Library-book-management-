# Generated by Django 3.2.19 on 2023-05-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll_number', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('year_of_admission', models.CharField(max_length=50)),
                ('email_ID', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_picture/')),
            ],
        ),
    ]