# Generated by Django 2.1.7 on 2022-01-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
