# Generated by Django 4.2.2 on 2023-06-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0004_college_leaderimage_univesity_leaderimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
