from rest_framework import viewsets, mixins, views, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *

from caisse.serializers import *
from plateau_technique.models import Lit
from plateau_technique.serializers import LitNestedSerializer

from compuclinic_api.settings import API_BASE_URL


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


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-date_creation')
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['est_interne', 'type', 'dossier']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return PatientNestedSerializer
        else:
            return PatientSerializer


class ListeQuittanceView(views.APIView):
    
    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            quittances = patient.quittance_set.all()
            serializer = QuittanceNestedSerializer(quittances, many=True, context={'request': request})
            return Response(serializer.data)
        except:
            return Response({'error': 'Pas de patient avec le pk fourni!'}, status=status.HTTP_417_EXPECTATION_FAILED)


class ListeBonView(views.APIView):
    
    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            bons = patient.bon_set.all()
            serializer = BonNestedSerializer(bons, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'error': 'Pas de patient avec le pk fourni!'}, status=status.HTTP_417_EXPECTATION_FAILED)


class InternementViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Internement.objects.all().order_by('-date_internement')
    serializer_class = InternementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient', 'lit__local', 'en_cours']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return InternementNestedSerializer
        else:
            return InternementSerializer
    
'''     def create(self, request):
        lits_libres = Lit.objects.filter(est_libre=True)
        if (len(lits_libres) == 0):
            return Response({'Message': "Il n'y a plus de lit disponible"})
        
        serializer = InternementSerializer(data=request.body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) '''




class InternerPatient(views.APIView):
    # TODO: Gérer de telle sorte que on recherche automatiquement un lit disponible, et on renvoie le lit disponible aussi.
    # TODO: Peut etre faudra t'il remplacer par un viewset Internement qui gérera l'internement et l'externement d'un patient.

    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': "Quelque chose ndem ici..."}, status=status.HTTP_400_BAD_REQUEST)
        patient.interner()
        if patient.est_interne:
            # Enregistrer l'internement
            lits =  Lit.objects.filter(est_libre=True)
            if len(lits) == 0:
                patient.externer()
                return Response({'status': 'echec', 'message': "il n'y a pas de lit disponible"}, status=status.HTTP_417_EXPECTATION_FAILED)
            else:
                internement = Internement(patient=patient)
                internement.find_lit()
                internement.save()
                lit = internement.lit
                return Response({'status': 'succès', 'message': 'Patient bien interné!', 'lit': {'id': lit.id, 'local': lit.local.nom, 'numero': lit.numero}})
        else:
            return Response(patient.get_empty_fields(), status=status.HTTP_417_EXPECTATION_FAILED)



class ExternerPatient(views.APIView):

    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': "Patient with id="+str(pk)+" does not exists!"}, status=status.HTTP_400_BAD_REQUEST)
            
        # On vérifie si il y a un internement en cours
        internements = Internement.objects.filter(patient=patient).filter(en_cours=True)
        
        if internements.count() == 0:
            patient.externer()
            return Response({"error": "Pas d'internement en cours! Externement manuel..."})
        
        # Si il y a trop d'internements, arreter le processus
        if internements.count() > 1:
            return Response({"error": "Trop d'internement! Corruption..."}, status=status.HTTP_417_EXPECTATION_FAILED)
        
        # On externe le patient (attribute level)
        patient.externer()
        
        if not patient.est_interne:
            # Libérer le lit et marqué en_cours comme false
            internement = internements[0]
            internement.sortir()
            return Response({'status': 'succès', 'message': 'Patient bien externé!'})
        else:
            return Response("chose s'est mal passé...", status=status.HTTP_417_EXPECTATION_FAILED)



# TODO: On doit pouvoir chercher un dossier en fonction des informations du patient. C'est pour vérifier si un patient n'a pas déjà un dossier dans la BD. Par exemple, en fontion de son nom, prenom, CNI, etc, on peut chercher les dossiers d'un patient
class DossierViewSet(viewsets.ModelViewSet):
    queryset = Dossier.objects.all().order_by('-date_creation')
    serializer_class = DossierSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['date_creation']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return DossierNestedSerializer
        else:
            return DossierSerializer


class ListePresenceViewSet(viewsets.ModelViewSet):
    queryset = ListePresence.objects.all().order_by('-date_creation')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient', 'valide', 'parametres_pris']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ListePresenceGetSerializer
        else:
            return ListePresencePostSerializer

