# Generated by Django 3.2.5 on 2021-08-30 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0009_remove_listepresence_nbre_quittances_non_consommees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listepresence',
            old_name='check_prise_parametre',
            new_name='parametres_pris',
        ),
    ]
