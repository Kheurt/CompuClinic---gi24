# Generated by Django 3.2.5 on 2021-09-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grh', '0013_alter_profilspecialiste_medecin'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='telephone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
