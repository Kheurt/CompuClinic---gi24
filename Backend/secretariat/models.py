from django.db import models
import uuid
from .enums import *
from datetime import datetime
from plateau_technique.models import Lit

class Patient(models.Model):
    SEXE = (
        ('H', 'Homme'),
        ('F', 'Femme')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default='')
    CNI = models.CharField(max_length=20, default='')
    sexe = models.CharField(max_length=1, choices=SEXE, default='H')
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=20, default='')
    telephone = models.CharField(max_length=15, default='')
    nationalite = models.CharField(max_length=50, default='Camerounais')
    profession = models.CharField(max_length=50, default='Eleve')
    lieu_travail = models.CharField(max_length=50, default='')
    telephone_lieu_travail = models.CharField(max_length=15, default='')
    domicile = models.CharField(max_length=20, default='')
    religion = models.CharField(choices=TYPE_RELIGION, max_length=20, default='')
    ethnie = models.CharField(max_length=50, default='')
    group_sanguin = models.CharField(choices=TYPE_GROUP_SANGUIN, max_length=10, default='')
    antecedent = models.TextField(default='')

    nom_garant = models.CharField(max_length=20, default='')
    prenom_garant = models.CharField(max_length=20, default='')
    telephone_garant = models.CharField(max_length=15, default='',)
    adresse_garant = models.CharField(max_length=50, default='')
    profession_garant = models.CharField(max_length=50, default='')
    lieu_travail_garant = models.CharField(max_length=50, default='')

    est_interne = models.BooleanField(default=False)
    type = models.CharField(choices=TYPE_PATIENT, max_length=10, default='Externe')
    date_creation = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "Patient: " + self.nom

    def get_empty_fields(self):
        res = []
        if self.prenom == '':
            res.append({'prenom': 'Le champ prenom est vide!'})
        if self.CNI == '':
            res.append({'CNI': 'Le champ CNI est vide!'})
        if self.date_naissance is None:
            res.append({'date_naissance': 'Le champ date_naissance est vide!'})
        if self.lieu_naissance == '':
            res.append({'prenom': 'Le champ prenom est vide!'})
        if self.telephone == '':
            res.append({'telephone': 'Le champ telephone est vide!'})
        if self.nationalite == '':
            res.append({'nationaliten': 'Le champ nationalite est vide!'})
        if self.profession == '':
            res.append({'profession': 'Le champ profession est vide!'})
        if self.lieu_travail == '':
            res.append({'lieu_travail': 'Le champ lieu_travail est vide!'})
        if self.domicile == '':
            res.append({'domicile': 'Le champ domicile est vide!'})
        if self.nom_garant == '':
            res.append({'nom_garant': 'Le champ nom_garant_ est vide!'})
        if self.prenom_garant == '':
            res.append({'prenom_garant': 'Le champ prenom_garant est vide!'})
        if self.telephone_garant == '':
            res.append({'telephone_garantl': 'Le champ telephone_garant est vide!'})
        if self.adresse_garant == '':
            res.append({'adresse_garant': 'Le champ adresse_garant est vide!'})
        if self.profession_garant == '':
            res.append({'profession_garant': 'Le champ profession_garant est vide!'})
        return res

    def perform_interner(self):
        empty_fields = self.get_empty_fields()
        if empty_fields != []:
            return False #TODO: Refactor this function to throw an exception
        else:
            self.est_interne = True
            self.type = 'Interne'
            return True

    def interner(self):
        if self.perform_interner():
            self.save()

    def externer(self):
        self.est_interne = False
        self.type = 'Externe'
        self.save()

    def save(self, *args, **kwargs):
        if self.matricule == '':
            self.matricule = self.generate_matricule()
        if self.est_interne:
            if self.perform_interner():
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def generate_matricule(self):
        # a patient matricule is a string of 14 characters:
        # the format : PAT[Name][Surname][Day]{2}[Month]{2}[Year]{2}[Number]{3}

        name = self.nom[0].upper()
        surname = '-'
        if self.prenom != '':
            surname = self.prenom[0].upper()
        today = datetime.now()
        day = today.day
        month = today.month
        year = today.year
        number = Patient.objects.count() + 1

        matricule = f"PAT{name}{surname}{day:02d}{month:02d}{year}{number:03d}"
        return matricule


class Dossier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    matricule = models.CharField(max_length=20, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False)
    patient = models.ForeignKey('Patient', db_column= 'patient_id', on_delete=models.SET_NULL, blank=False, null=True)
    # patient = models.OneToOneField('Patient', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Dossier " + self.matricule

    def save(self, *args, **kwargs):
        self.matricule = self.generate_matricule()
        super().save(*args, **kwargs)

    def generate_matricule(self):
        # a patient matricule is a string of 14 characters:
        # the format : DOS[Day]{2}[Month]{2}[Year]{2}[Number]{3}

        today = datetime.now()
        day = today.day
        month = today.month
        year = today.year
        number = Dossier.objects.count() + 1

        matricule = f"DOS{day:02d}{month:02d}{year}{number:03d}"
        return matricule


class ListePresence(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True)
    # patient = models.OneToOneField('Patient', on_delete=models.SET_NULL, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False)
    parametres_pris = models.BooleanField(default=False)
    valide = models.BooleanField(default=False)
    colorpatient = models.BooleanField(default=False)
    prescription = models.ForeignKey('consultation.PrescriptionExamen', on_delete=models.SET_NULL, null=True)
    
    @classmethod
    def valider_patient(cls, patient_instance):
        """
            Cette Méthode rend un patient éligible aux soins médicaux, car a payé.
            Elle renvoie False si quelque chose c'est mal passé lors de la validation, et True sinon
        """
        instance = None
        try:
            instance = cls.objects.get(patient=patient_instance)
        except:
            # Le patient n'est pas dans la liste de présence
            return False
        
        # Le patient est dans la liste de présence, on le valide
        instance.valide = True
        instance.save()
        return True


class Internement(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True)
    lit = models.ForeignKey('plateau_technique.Lit', on_delete=models.SET_NULL, null=True)
    date_internement = models.DateTimeField(auto_now_add=True, editable=False)
    date_sortie = models.DateTimeField(null=True, default=None)
    en_cours = models.BooleanField(default=True)
    
    def find_lit(self):
        lits = Lit.objects.filter(est_libre=True)
        if lits.count() == 0:
            return False
        lit = lits[0]
        lit.est_libre = False
        
        # Affecter le lit au patient
        self.lit = lit
        
        # Sauvegarder le tout
        lit.save()
    
    def liberer_lit(self):
        self.lit.est_libre = True
        self.lit.save()
    
    def sortir(self):
        self.liberer_lit()
        self.en_cours = False
        self.date_sortie = datetime.now()
        self.save()
    
    def delete(self, *args, **kwargs):
        # Libérer le lit
        self.lit.est_libre = True
        self.lit.save()
        
        super().delete(*args, **kwargs)
