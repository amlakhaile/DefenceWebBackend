# Generated by Django 4.2.2 on 2023-06-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='bannerimage',
            field=models.ImageField(upload_to='collage'),
        ),
        migrations.AlterField(
            model_name='department',
            name='photo',
            field=models.ImageField(upload_to='collage'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='photo',
            field=models.ImageField(upload_to='collage'),
        ),
    ]
