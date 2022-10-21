from secretariat.models import Patient
from rest_framework import viewsets, mixins, views, status
from rest_framework.filters import SearchFilter, OrderingFilter
from  rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
import json


class EnumView(views.APIView):
    
    def get(self, request):
        param = request.query_params.get('type')
        
        # Liste des Enums
        if param is None:
            return Response(LISTE_ENUM)
        
        # Récupérer un enum
        if param in LISTE_ENUM.keys():
            res = LISTE_ENUM[param]
            return Response(res)
        else:
            return Response({'error': 'Pas d\'enum de ce type'}, status=status.HTTP_400_BAD_REQUEST)

class BonViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Bon.objects.all().order_by('-date_creation')
    serializer_class = BonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['prestataire', 'patient', 'est_consommee']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BonNestedSerializer
        else:
            return BonSerializer


class AGVViewSet(viewsets.ModelViewSet):
    queryset = AGV.objects.all().order_by('-date_creation')
    serializer_class = AGVSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['prestataire', 'patient', 'est_consommee']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return AGVNestedSerializer
        else:
            return AGVSerializer


class BGSViewSet(viewsets.ModelViewSet):
    queryset = BGS.objects.all().order_by('-date_creation')
    serializer_class = BGSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['prestataire', 'patient', 'est_consommee']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BGSNestedSerializer
        else:
            return BGSSerializer


class BSCViewSet(viewsets.ModelViewSet):
    queryset = BSC.objects.all().order_by('-date_creation')
    serializer_class = BSCSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['prestataire', 'patient', 'est_consommee']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BSCNestedSerializer
        else:
            return BSCSerializer


class TIAPSViewSet(viewsets.ModelViewSet):
    queryset = TIAPS.objects.all().order_by('-date_creation')
    serializer_class = TIAPSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['medecin', 'est_utilise', 'type', 'numero_tiaps']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TIAPSNestedSerializer
        else:
            return TIAPSSerializer


class QuittanceViewSet(viewsets.ModelViewSet):
    queryset = Quittance.objects.all().order_by('-date_creation')
    serializer_class = QuittanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient', 'numero', 'caissier', 'est_consommee']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return QuittanceNestedSerializer
        else:
            return QuittanceSerializer


class QuittancePatientView(views.APIView):
    
    def get(self, request):
        data = json.loads(request.body)
        print(data)
        request_serializer = QuittancePatientRequestSerializer(data=data)
        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        id = request_serializer.data['patient']
        number_only = request_serializer.data['number_only']
        patient = Patient.objects.filter(id=id)
        if patient.count() == 0:
            return Response({"Message": "Le patient avec cet id n'existe pas!"}, status=status.HTTP_417_EXPECTATION_FAILED)

        patient = patient[0]
        quittances = Quittance.objects.filter(patient=patient).filter(est_consommee=False)
        number = quittances.count()
        
        res = None
        if number_only:
            res = {'number': number}
        else:
            res = {'number': number, 'quittances':  list(quittances)}
    
        response_serializer = QuittancePatientResponseSerializer(data=res)
        
        if response_serializer.is_valid():
            return Response(response_serializer.data)
        else:
            return Response(response_serializer.errors)