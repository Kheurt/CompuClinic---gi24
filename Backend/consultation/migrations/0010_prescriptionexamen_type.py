# Generated by Django 3.2.5 on 2021-09-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0009_auto_20210906_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptionexamen',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
