# Generated by Django 4.2.2 on 2023-07-06 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0021_department_academicgoals_department_academicprogram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colleges.college'),
        ),
    ]