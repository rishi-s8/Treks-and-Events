# Generated by Django 2.0 on 2017-12-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_event_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pics',
            name='credits',
            field=models.CharField(default='IDK', max_length=200),
        ),
        migrations.AlterField(
            model_name='pics',
            name='file_type',
            field=models.CharField(default='jpg', max_length=10),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='credits',
            field=models.CharField(default='IDK', max_length=200),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='file_type',
            field=models.CharField(default='jpg', max_length=10),
        ),
    ]
