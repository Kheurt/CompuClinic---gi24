# Generated by Django 3.2.5 on 2021-09-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grh', '0017_auto_20210907_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/personnels/'),
        ),
    ]
