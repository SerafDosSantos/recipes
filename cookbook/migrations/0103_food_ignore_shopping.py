# Generated by Django 3.1.5 on 2021-01-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0102_auto_20210125_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ignore_shopping',
            field=models.BooleanField(default=False),
        ),
    ]