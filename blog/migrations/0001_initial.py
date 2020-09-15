# Generated by Django 3.1 on 2020-09-15 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
    ]
