# Generated by Django 3.2.5 on 2021-08-01 10:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=15)),
                ('prestation', models.CharField(choices=[('Q-CONSULT', 'Consultation'), ('Q-EXAM', 'Examen'), ('Q-PHARMA', 'Pharmacie'), ('Q-SA', 'Q-SA'), ('Q-SI', 'Q-SI'), ('Q-DIV', 'Q-DIV'), ('Q-FD', 'Q-FD')], max_length=20)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_limite_validite', models.DateTimeField(blank=True, null=True)),
                ('est_consommee', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quittance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=15)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('prestation', models.CharField(choices=[('Q-CONSULT', 'Consultation'), ('Q-EXAM', 'Examen'), ('Q-PHARMA', 'Pharmacie'), ('Q-SA', 'Q-SA'), ('Q-SI', 'Q-SI'), ('Q-DIV', 'Q-DIV'), ('Q-FD', 'Q-FD')], max_length=20)),
                ('rubrique', models.CharField(choices=[('MG-CO', 'Consultation par médecin généraliste'), ('MG-CRV', 'Consultation sur Rendez-vous par médecin généraliste'), ('MS-CO', 'Consultation par médecin spécialiste'), ('MS-CRV', 'Consultation sur Rendez-vous par médecin spécialiste')], max_length=20)),
                ('montant_TTC', models.PositiveIntegerField()),
                ('remise', models.IntegerField(default=0)),
                ('montant_net', models.IntegerField(default=0)),
                ('est_consommee', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AGV',
            fields=[
                ('bon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='caisse.bon')),
            ],
            bases=('caisse.bon',),
        ),
        migrations.CreateModel(
            name='BGS',
            fields=[
                ('bon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='caisse.bon')),
            ],
            bases=('caisse.bon',),
        ),
        migrations.CreateModel(
            name='BSC',
            fields=[
                ('bon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='caisse.bon')),
                ('raison_credit', models.TextField()),
                ('garantie', models.TextField()),
            ],
            bases=('caisse.bon',),
        ),
        migrations.CreateModel(
            name='TIAPS',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero_tiaps', models.CharField(max_length=20)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_limite_validite', models.DateTimeField(blank=True, default=None, null=True)),
                ('type', models.CharField(choices=[('QUITTANCE', 'TIAPS pour Quittance'), ('BON', 'TIAPS pour Bon')], default='QUITTANCE', max_length=10)),
                ('est_utilise', models.BooleanField(default=False)),
                ('bon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='caisse.bon')),
            ],
        ),
    ]
