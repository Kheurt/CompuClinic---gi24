# Generated by Django 3.2.5 on 2022-06-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0029_alter_prescriptionexamen_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptionexamen',
            name='type',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
