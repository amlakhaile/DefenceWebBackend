# Generated by Django 4.2.2 on 2023-06-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0002_alter_college_bannerimage_alter_department_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Univesity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderName', models.CharField(max_length=70)),
                ('welcomeMessage', models.TextField()),
                ('about', models.TextField()),
                ('adminstartion', models.TextField()),
                ('pathname', models.CharField(max_length=10)),
                ('bannerimage', models.ImageField(upload_to='collage')),
            ],
        ),
    ]
