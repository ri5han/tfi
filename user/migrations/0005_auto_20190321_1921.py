# Generated by Django 2.1.7 on 2019-03-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190321_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='commitment_needed',
            field=models.IntegerField(default=2),
        ),
    ]
