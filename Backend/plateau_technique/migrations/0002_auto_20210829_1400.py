# Generated by Django 3.2.5 on 2021-08-29 13:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('grh', '0005_remove_poste_unite'),
        ('plateau_technique', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('libre', models.BooleanField(default=True)),
                ('local', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateau_technique.local')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='local',
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='plateau_technique.local'),
        ),
        migrations.AddField(
            model_name='service',
            name='specialite',
            field=models.CharField(choices=[('URGENCE PREADMISION', 'Unité de Préadmission'), ('URGENCE MED', 'Unité des urgences médicales'), ('URGENCE CHIR', 'Unité des urgences chirurgicales'), ('CONSULT MED', 'Unité des Consultations médicales des explorations fonctionnelles'), ('CONSULT CHIR', 'Unité des Consultations chirurgicales'), ('GYN-OBST', 'Unité des Consultations gynéco-obstétricales'), ('CONSULT STOMATO', 'Unité des Consultations stomatologiques'), ('CONSULT OPHTALMO', 'Unité des Consultations ophtalmologiques'), ('CONSULT ORL', 'Unité des Consultations otorhinolaryngologiques '), ('HOSPI MED', 'Unité d hospitalisation médicale'), ('HOSPI CHIR', 'Unité d hospitalisation chirurgicale '), ('HOSPI GYN', 'Unité d hospitalisation Gynéco-obstétricale '), ('HOSPI PEDIA', 'Unité d hospitalisation pédiatrique '), ('HOSPI PEDIA', 'Unité d hospitalisation VIP '), ('HOSPI PSY', 'Unité d hospitalisation psychiatrique '), ('HOSPI REHABIL', 'Unité d hospitalisation réhabilitation '), ('HOSPI REA', 'Unité d hospitalisation Réanimation '), ('HOSPI HEMODIA', 'Unité d hospitalisation Hémodialyse '), ('BLOC OP', 'Unité Bloc opératoire '), ('BLOC STERI', 'Unité de Stérilisation centrale '), ('BLOC SPI', 'Unité de Stérilisation centrale '), ('BLOC OBST', 'Unité Bloc obstétrical '), ('ANESTH', 'Unité d anesthésie '), ('HOSPI REA', 'Unité de réanimation '), ('LAB ANALYSES', 'Unité d analyses biomédicales courantes '), ('LAB TRANSFUSION', 'Unité de Tansfusion sanguine '), ('LAB BIOMOLECULAIRE', 'Unité de biologie moléculaire '), ('IMAG RADIO', 'Unité de radiologie conventionnelle'), ('IMAG SCANNER', 'Unité  Scanner '), ('IMAG IRM', 'Unité IRM '), ('IMAG ECHO', 'Unité d échographie '), ('IMAG GAMMA', 'Unité Gamma camera '), ('ANAPATH HISTO', 'Unité d histopathologie '), ('ANAPATH MEDICO LEGAL', 'Unité de médecine légale '), ('PHYSIOTHER PHYSIO', 'Unité de Physiothérapie '), ('PHYSIOTHER KINE', 'Unité de Kinésithérapie '), ('PHYSIOTHER ERGOT', 'Unité d ergothérapie '), ('RADIOTHER EXT', 'Unité de radiothérapie externe '), ('RADIOTHER CONTACT', 'Unité de radiothérapie de contact '), ('RADIOTHER ISOTOPE', 'Unité de radiothérapie isotopique ')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('DIRECTION MEDICALE', 'Direction médicale'), ('DIRECTION PARAMÉDICALE', 'Direction paramédicale'), ('SERVICE URGENCES', 'Service des Urgences'), ('SERVICE CONSULTATIONS  Externes & Soins ambulatoires', 'Service des Consultations  Externes & Soins ambulatoires'), ('SERVICE HOSPITALISATION', 'SERVICE DES HOSPITALISATION'), ('SERVICE BLOC TECHNIQUE', 'SERVICE BLOC TECHNIQUE'), ('SERVICE ANESTHESIE-REANIMATION', 'SERVICE D ANESTHESIE-REANIMATION'), ('SERVICE LABORATOIRE BIOMEDICAL', 'SERVICE DE LABORATOIRE BIOMEDICAL'), ('SERVICE IMAGERIE MEDICALE', 'SERVICE D IMAGERIE MEDICALE'), ('SERVICE PHYSIOTHERAPIE REEDUCATION FONCTIONNELLE', 'SERVICE DE PHYSIOTHERAPIE REEDUCATION FONCTIONNELLE'), ('SERVICE RADIOTHERAPIE', 'SERVICE DE RADIOTHERAPIE')], max_length=255),
        ),
        migrations.DeleteModel(
            name='UniteMedicale',
        ),
    ]