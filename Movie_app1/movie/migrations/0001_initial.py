# Generated by Django 5.2 on 2025-05-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='movie')),
                ('movie_name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
