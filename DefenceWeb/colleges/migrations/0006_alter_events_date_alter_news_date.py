# Generated by Django 4.2.2 on 2023-06-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("colleges", "0005_alter_news_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="news",
            name="date",
            field=models.DateField(),
        ),
    ]
