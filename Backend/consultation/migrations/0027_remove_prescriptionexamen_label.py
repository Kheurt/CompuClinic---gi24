# Generated by Django 3.2.5 on 2022-06-17 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0026_auto_20220617_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescriptionexamen',
            name='label',
        ),
    ]
