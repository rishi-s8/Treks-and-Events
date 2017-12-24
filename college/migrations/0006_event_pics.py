# Generated by Django 2.0 on 2017-12-24 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_trek_card_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('logo_link', models.CharField(default='', max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('credits', models.CharField(max_length=200)),
                ('file_link', models.CharField(default='', max_length=1500)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Event')),
            ],
        ),
    ]