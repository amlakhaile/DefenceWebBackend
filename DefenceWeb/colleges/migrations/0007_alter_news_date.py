# Generated by Django 4.2.2 on 2023-06-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("colleges", "0006_alter_events_date_alter_news_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]