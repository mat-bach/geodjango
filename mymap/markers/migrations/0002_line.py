# Generated by Django 4.2.7 on 2023-11-29 17:14

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
    ]
