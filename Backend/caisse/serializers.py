from .models import *
from rest_framework import serializers
from grh.serializers import LaborantinSerializer, PersonnelSerializer, CaissierSerializer, MedecinSerializer
from secretariat.serializers import PatientSerializer
from plateau_technique.serializers import ServiceSerializer


class BonNestedSerializer(serializers.ModelSerializer):
    prestataire = PersonnelSerializer()
    patient = PatientSerializer()

    class Meta:
        model = Bon
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )


class BonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bon
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']



class AGVSerializer(serializers.ModelSerializer):
    class Meta:
        model = AGV
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class AGVNestedSerializer(serializers.ModelSerializer):
    prestataire = PersonnelSerializer()
    patient = PatientSerializer()

    class Meta:
        model = AGV
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )

class BGSSerializer(serializers.ModelSerializer):
    class Meta:
        model = BGS
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class BGSNestedSerializer(serializers.ModelSerializer):
    prestataire = PersonnelSerializer()
    patient = PatientSerializer()

    class Meta:
        model = BGS
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )


class BSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = BSC
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class BSCNestedSerializer(serializers.ModelSerializer):
    prestataire = PersonnelSerializer()
    patient = PatientSerializer()

    class Meta:
        model = BSC
        read_only_fields = ['numero', 'id', 'date_creation', 'date_limite_validite', 'est_consommee']
        extra_kwargs = {
            'est_consommee': {
                'required': False,
            }
        }
        exclude = ('_tiaps_generated', )


class QuittanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quittance
        read_only_fields = ['numero', 'id', 'date_creation', 'est_consommee']
        exclude = ('_tiaps_generated', )

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class QuittanceNestedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    caissier = CaissierSerializer()

    class Meta:
        model = Quittance
        read_only_fields = ['numero', 'id', 'date_creation', 'est_consommee']
        exclude = ('_tiaps_generated', '_counted')

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class QuittanceNestedTIAPSSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    
    class Meta:
        model = Quittance
        exclude = ('_tiaps_generated', '_counted')


class TIAPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TIAPS
        fields = '__all__'
        read_only_fields = ['numero_tiaps', 'id', 'date_creation', 'date_limite_validite']
        extra_kwargs = {
            'est_utilisee': {
                'default': False,
            }
        }

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class TIAPSNestedSerializer(serializers.ModelSerializer):
    medecin = MedecinSerializer()
    quittance = QuittanceNestedTIAPSSerializer()
    bon = BonNestedSerializer()
    laborantin=LaborantinSerializer()

    class Meta:
        model = TIAPS
        fields = '__all__'
        read_only_fields = ['numero_tiaps', 'id', 'date_creation', 'date_limite_validite']
        extra_kwargs = {
            'est_utilisee': {
                'default': False,
            }
        }

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class QuittancePatientRequestSerializer(serializers.Serializer):
    patient = serializers.UUIDField()
    number_only = serializers.BooleanField(required=False, default=False)


class QuittancePatientResponseSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    quittances = QuittanceNestedSerializer(many=True, required=False)
