# Generated by Django 4.2.2 on 2023-06-25 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('leaderName', models.CharField(max_length=70)),
                ('welcomeMessage', models.TextField()),
                ('about', models.TextField()),
                ('adminstartion', models.TextField()),
                ('pathname', models.CharField(max_length=10)),
                ('bannerimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HelpTexts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.college')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=70)),
                ('type', models.CharField(choices=[('Announcment', 'Announcment'), ('Research', 'Research'), ('News', 'News')], default='News', max_length=13)),
                ('image', models.ImageField(null=True, upload_to='news')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='colleges.college')),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facilityname', models.CharField(max_length=70)),
                ('Facilities_detail', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='facilities')),
                ('collage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.college')),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.college')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityOutreach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.news')),
            ],
        ),
    ]
