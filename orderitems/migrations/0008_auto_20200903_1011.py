# Generated by Django 3.0 on 2020-09-03 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderitems', '0007_auto_20200903_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitems',
            old_name='quantitty',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='createdDate',
            field=models.DateField(default=datetime.datetime(2020, 9, 3, 10, 11, 31, 22848)),
        ),
    ]