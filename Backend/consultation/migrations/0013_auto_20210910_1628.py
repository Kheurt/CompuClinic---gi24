# Generated by Django 3.2.5 on 2021-09-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0012_alter_consultation_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='label',
        ),
        migrations.AddField(
            model_name='prescriptionmedicamenteuse',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recommandation',
            name='label',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='prescriptionmedicamenteuse',
            name='duree',
            field=models.CharField(max_length=100),
        ),
    ]
