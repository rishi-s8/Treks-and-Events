# Generated by Django 2.0 on 2017-12-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20171222_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='file_link',
            field=models.CharField(default='', max_length=1500),
        ),
    ]
