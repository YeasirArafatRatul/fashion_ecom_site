# Generated by Django 3.1 on 2020-09-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20200922_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='account_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='trlxid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_system',
            field=models.CharField(choices=[('CashOnDelivery', 'CashOnDelivery'), ('bKash', 'bKash')], max_length=30),
        ),
    ]