# Generated by Django 3.1 on 2020-09-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSettings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
