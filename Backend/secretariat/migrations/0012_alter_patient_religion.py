# Generated by Django 3.2.5 on 2021-09-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0011_internement_en_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='religion',
            field=models.CharField(choices=[('Chrétien', 'Chrétien'), ('Musulman', 'Musulman'), ('Boudiste', 'Boudiste'), ('Athée', 'Athée'), ('Animiste', 'Animiste')], default='', max_length=20),
        ),
    ]
