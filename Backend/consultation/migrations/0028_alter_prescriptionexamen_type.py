# Generated by Django 3.2.5 on 2022-06-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0027_remove_prescriptionexamen_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptionexamen',
            name='type',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
