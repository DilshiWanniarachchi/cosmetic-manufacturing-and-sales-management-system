# Generated by Django 4.1.2 on 2022-11-04 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerAndSalesManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 9, 46, 31, 246670)),
        ),
    ]
