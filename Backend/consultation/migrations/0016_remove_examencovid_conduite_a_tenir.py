# Generated by Django 3.2.5 on 2022-01-26 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0015_examencovid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examencovid',
            name='Conduite_a_tenir',
        ),
    ]
