# Generated by Django 3.2.19 on 2023-05-15 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userHandler', '0001_initial'),
        ('bookHandler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_units', models.IntegerField(default=0)),
                ('total_used', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookHandler.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookBorrowDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('total_number_of_days', models.IntegerField(default=15)),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('is_fine_cleared', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookHandler.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userHandler.student')),
            ],
        ),
    ]
