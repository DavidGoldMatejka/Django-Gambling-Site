# Generated by Django 3.0.4 on 2020-05-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='coins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]