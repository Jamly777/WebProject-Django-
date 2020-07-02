# Generated by Django 3.0.7 on 2020-06-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='life',
            fields=[
                ('date', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('kongtiao', models.CharField(max_length=255)),
                ('yundong', models.CharField(max_length=255)),
                ('ziwaixian', models.CharField(max_length=255)),
                ('ganmao', models.CharField(max_length=255)),
                ('chuanyi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='realtime',
            fields=[
                ('date', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=255)),
                ('windspeed', models.CharField(max_length=255)),
                ('direct', models.CharField(max_length=255)),
                ('power', models.CharField(max_length=255)),
                ('humidity', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=255)),
                ('temperature', models.CharField(max_length=255)),
            ],
        ),
    ]
