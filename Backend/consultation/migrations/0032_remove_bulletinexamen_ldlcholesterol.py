# Generated by Django 3.2.5 on 2022-06-20 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0031_auto_20220619_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletinexamen',
            name='ldlcholesterol',
        ),
    ]