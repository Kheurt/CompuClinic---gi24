# Generated by Django 3.2.5 on 2022-06-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0032_remove_bulletinexamen_ldlcholesterol'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptionexamen',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
