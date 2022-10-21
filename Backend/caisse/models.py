
from secretariat.models import Dossier, ListePresence
from django.db import models
from .enums import *
import uuid
from datetime import timedelta, date
from datetime import datetime as datetime_class
from grh.models import *


class Bon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.CharField(max_length=15)
    prestataire = models.ForeignKey('grh.Personnel', on_delete=models.CASCADE, help_text="Personnel qui délivre le bon")
    patient = models.ForeignKey('secretariat.Patient', on_delete=models.SET_NULL, null=True)
    prestation = models.CharField(max_length=20, choices=PRESTATIONS)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_limite_validite = models.DateField(blank=True, null=True)
    est_consommee = models.BooleanField(default=False)
    _tiaps_generated = models.BooleanField(default=False)

    def consommer(self):
        self.est_consommee = True
        self._tiaps_generated = True
        self.save()

    def save(self, *args, **kwargs):
        # On génère un numéro de dossier
        if self.numero is None or self.numero == "":
            self.numero = self.generate_numero()
        
        # On défini la date limite de validité à today + 30j
        days_30_delay = timedelta(days=30)
        today = date.today()
        self.date_limite_validite = today + days_30_delay
        

        # On met a jour la liste de présence
        retour = ListePresence.valider_patient(self.patient)
        if retour is False:
            # Quelque chose s'est mal passé. Le patient n'est pas dans la liste d'attente
            return "Error: Le patient n'est pas dans la liste d'attente"
        
        # entree_liste_presence = ListePresence.objects.get(patient=self.patient)
        # entree_liste_presence.a_paye = True
        # entree_liste_presence.save()

        # On teste si le patient a un dossier. Si il n'en a pas, on en crée un
        try:
            if self.patient.dossier is not None:
                pass
        except AttributeError :
            dossier = Dossier(patient=self.patient)
            dossier.save()
            self.patient.dossier = dossier
        finally:
            super().save(*args, **kwargs)


class AGV(Bon):
    # TODO: redéfinir la méthode save pour vérifier que c'est bien un prestataire de type médecin qui essaie de créer le Bon

    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)
        
        # Generate a TIAPS
        if not self._tiaps_generated:
            self.generate_TIAPS()
            self._tiaps_generated = True
        


    def generate_TIAPS(self):
        # Générer un TIAPS et lier ce TIAPS au prestataire
        medecin = Medecin.objects.get(pk=self.prestataire.id)
        tiaps = TIAPS(
            medecin=medecin,
            type='AGV',
            bon=self,
        )
        tiaps.save()
        

    def generate_numero(self):
        # a AGV.numero is a string of 14 characters:
        # the format : AGV[Day]{2}[Month]{2}[Year]{2}[Number]{3}

        today = datetime_class.now()
        day = today.day
        month = today.month
        year = today.year
        number = AGV.objects.count() + 1

        matricule = f"AGV{day:02d}{month:02d}{year}{number:03d}"
        return matricule


class BGS(Bon):
    # TODO: redéfinir la méthode save pour vérifier que c'est bien un prestataire de type direction qui essaie de créer le Bon

    def generate_numero(self):
        # a AGV.numero is a string of 14 characters:
        # the format : AGV[Day]{2}[Month]{2}[Year]{2}[Number]{3}

        today = datetime_class.now()
        day = today.day
        month = today.month
        year = today.year
        number = BGS.objects.count() + 1

        matricule = f"BGS{day:02d}{month:02d}{year}{number:03d}"
        return matricule


class BSC(Bon):
    # TODO: redéfinir la méthode save pour vérifier que c'est bien un prestataire de type direction qui essaie de créer le Bon
    raison_credit = models.TextField()
    garantie = models.TextField()

    def generate_numero(self):
        # a AGV.numero is a string of 14 characters:
        # the format : AGV[Day]{2}[Month]{2}[Year]{2}[Number]{3}

        today = datetime_class.now()
        day = today.day
        month = today.month
        year = today.year
        number = BSC.objects.count() + 1

        matricule = f"BSC{day:02d}{month:02d}{year}{number:03d}"
        return matricule


class TIAPS(models.Model):
    TYPE_TIAPS = (
        ('QUITTANCE', 'TIAPS pour Quittance'),
        ('AGV', 'TIAPS pour AGV'),
        ('BGS', 'TIAPS pour BGS'),
        ('BSC', 'TIAPS pour BSC'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_tiaps = models.CharField(max_length=20)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_limite_validite = models.DateTimeField(null=True, blank=True, default=None)
    medecin = models.ForeignKey('grh.Medecin', on_delete=models.CASCADE , null=True)
    laborantin = models.ForeignKey('grh.Laborantin', on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, choices=TYPE_TIAPS, default='QUITTANCE')
    quittance = models.ForeignKey('Quittance', on_delete=models.CASCADE, null=True)
    bon = models.ForeignKey('Bon', on_delete=models.CASCADE, null=True)
    date_consultation = models.DateField(default=None, null=True)
    heure_debut = models.TimeField(default=None, null=True)
    heure_fin = models.TimeField(default=None, null=True)
    est_utilise = models.BooleanField(default=False)

    # TODO: Lors de la création d'un TIAPS, il faut marquer comme consommé la quittance ou le bon utilisé

    def save(self, *args, **kwargs):
        # Generate the matricule
        if self.numero_tiaps is None or self.numero_tiaps == "":
            self.numero_tiaps = self.generate_numero()     
        
        # Consommer le bon ou la quittance
        self.consommer_bon_ou_quittance()
        super().save(*args, **kwargs)

    @classmethod
    def utiliser(cls, patient):
        # 1. Chercher un Tiaps non utilisé pour le patient
        # 1.1. Chercher les quittances et les bons du patient
        quittances = Quittance.objects.filter(patient=patient)
        bons = Bon.objects.filter(patient=patient)
        
        tiaps = cls.objects.all()
        
        tiaps_pour_bons = tiaps.filter(type="BON").filter(bon__in=bons).filter(est_utilise=False)
        tiaps_pour_quittances = tiaps.filter(type="QUITTANCE").filter(quittance__in=quittances).filter(est_utilise=False)
        
        used_tiaps = None
        
        if tiaps_pour_bons.count() !=  0:
            # Il y des tiaps pour bon  non consommés. On l'utilise
            used_tiaps = tiaps_pour_bons[0]

        elif tiaps_pour_quittances.count() != 0:
            used_tiaps = tiaps_pour_quittances[0]
        
        if used_tiaps is not None:
            used_tiaps.est_utilise = True
            used_tiaps.save()
            return True
        else:
            return False    
        # alt-2: Il n'y a pas de TIAPS non utilisé au nom du patient: lever une exception TIAPSNonUtilizedForPatientEmpty
        # 2. Marquer le Tiaps comme utilisé

    def consommer_bon_ou_quittance(self):
        if self.type == "QUITTANCE":
            self.quittance.consommer()
        else:
            self.bon.consommer()

    def generate_numero(self):
        # a AGV.numero is a string of 14 characters:
        # the format : AGV[Day]{2}[Month]{2}[Year]{2}[Number]{3}

        today = datetime_class.now()
        day = today.day
        month = today.month
        year = today.year
        number = TIAPS.objects.count() + 1

        matricule = f"TIAPS{day:02d}{month:02d}{year}{number:03d}"
        return matricule


class Quittance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('secretariat.Patient', on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)
    date_creation = models.DateTimeField(auto_now_add=True)
    caissier = models.ForeignKey('grh.Caissier', on_delete=models.CASCADE)
    prestation = models.CharField(max_length=20, choices=PRESTATIONS)
    rubrique = models.CharField(max_length=20, choices=RUBRIQUES)
    montant_TTC = models.PositiveIntegerField(null=False)
    remise = models.IntegerField(default=0)
    montant_net = models.IntegerField(default=0, null=False)
    est_consommee = models.BooleanField(default=False)
    _counted = models.BooleanField(default=False)
    _tiaps_generated = models.BooleanField(default=False)

    def consommer(self):
        self.est_consommee = True
        self._tiaps_generated = True
        self.save()

    def save(self, *args, **kwargs):
        # On génère un numéro de quittance
        if self.numero is None or self.numero == "":
            self.numero = self.generate_numero()

        # On met a jour la liste de présence
        # if not self._counted:
        #     entree_liste_presence = ListePresence.objects.get(patient=self.patient)
        #     entree_liste_presence.increment_nbr_quittance_non_consommee()
        #     entree_liste_presence.save()
        #     self._counted = True

        # On teste si le patient a un dossier. Si il n'en a pas, on en crée un
        try:
            if self.patient.dossier is not None:
                pass
        except AttributeError :
            dossier = Dossier(patient=self.patient)
            dossier.save()
            self.patient.dossier = dossier
        finally:
            super().save(*args, **kwargs)


    @classmethod
    def nbre_quittances_non_consommees(cls, patient_instance):
        res = cls.objects.filter(patient=patient_instance).filter(est_consommee=False).count()
        return res

    def generate_numero(self):
        # a AGV.numero is a string of 14 characters:
        # the format : AGV[Day]{2}[Month]{2}[Year]{2}[Number]{3}

        today = datetime_class.now()
        day = today.day
        month = today.month
        year = today.year
        number = AGV.objects.count() + 1

        matricule = f"QTC{day:02d}{month:02d}{year}{number:03d}"
        return matricule
