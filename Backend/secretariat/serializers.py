from .models import *
from rest_framework import serializers
from plateau_technique.serializers import LitNestedSerializer


class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossier
        fields = '__all__'
        read_only_fields = ['matricule', 'date_creation']

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class PatientSerializer(serializers.ModelSerializer):
    dossier = DossierSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['matricule', 'date_creation']

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']

class DossierNestedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    
    class Meta:
        model = Dossier
        fields = '__all__'


class PatientNestedSerializer(serializers.ModelSerializer):
    dossier = DossierSerializer()
    
    class Meta:
        model  = Patient
        fields = '__all__'


class ListePresenceGetSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = ListePresence
        fields = '__all__'
        read_only_fields = ['a_paye', 'date_creation', 'nbre_quittances_non_consommees']


class ListePresencePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListePresence
        fields = '__all__'
        read_only_fields = ['a_paye', 'date_creation', 'nbre_quittances_non_consommees']


class InternementSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Internement
        fields = '__all__'
        read_only_fields = ['lit', 'date_internement']

class InternementNestedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    lit = LitNestedSerializer()
    
    class Meta:
        model = Internement
        fields =  '__all__'
        read_only_fields = ['lit', 'date_internement']

