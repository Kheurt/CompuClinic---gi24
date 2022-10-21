from rest_framework import viewsets, views, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
import json

# TODO: Modifier la vue des consultations pour qu'on puisse directement voir ses composants : parametres, Differentiel, prescriptions, examens, ...

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


class FermerConsultationView(views.APIView):
    
    def post(self, request, pk):
        consultation = Consultation.objects.filter(pk=pk)
        if consultation.count() == 0:
            return Response({'error': "Pas de consultation existante avec cet id!"}, status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            consultation = consultation[0]
            consultation.fermer()
            return Response({"Succes": "Consultation bien fermée!"})

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all().order_by('-date_creation')
    serializer_class = ConsultationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'en_cours', 'date_creation', 'dossier', 'medecin', 'dossier__patient']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ConsultationNestedSerializer
        else:
            return ConsultationSerializer

class  BulletinExamenViewSet(viewsets.ModelViewSet):
    queryset = BulletinExamen.objects.all()
    serializer_class =  BulletinExamenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','date_prelevement','resultat','laborantin','consultation', 'prescription']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
          return BulletinExamenNestedSerializer
        else:
            return BulletinExamenSerializer


# TODO: Il faut bien verifier que seuls les médecins et les infirmiers peuvent prendre les parametres
class ParametreViewSet(viewsets.ModelViewSet):
    queryset = Parametre.objects.all()
    serializer_class = ParametreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation', 'auteur']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ParametreNestedSerializer
        else:
            return ParametreSerializer


class ParametreBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = ParametreSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)

class SymptomeViewSet(viewsets.ModelViewSet):
    queryset = Symptome.objects.all()
    serializer_class = SymptomeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation']


class SymptomeBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = SymptomeSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)

class DifferentielViewSet(viewsets.ModelViewSet):
    queryset = Differentiel.objects.all()
    serializer_class = DifferentielSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation']


class DifferentielBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = DifferentielSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)


class RecommandationViewSet(viewsets.ModelViewSet):
    queryset = Recommandation.objects.all()
    serializer_class = RecommandationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation']
    
class RecommandationBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = RecommandationSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)


class PrescriptionExamenViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionExamen.objects.all()
    serializer_class = PrescriptionExamenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['est_fait' , 'consultation', 'type', 'description' ,'id']


    
class PrescriptionExamenBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = PrescriptionExamenSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)



class PrescriptionMedicamenteuseViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionMedicamenteuse.objects.all()
    serializer_class = PrescriptionMedicamenteuseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation']


class PrescriptionMedicamenteuseBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = PrescriptionMedicamenteuseSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)


class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation', 'prescription','laborantin','est_fait']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
          return ExamenNestedSerializer
        else:
          return ExamenSerializer
    
class ExamenBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = ExamenSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend]


class TestBulkCreateView(views.APIView):
    
    def post(self, request):
        body = request.body.decode('utf-8')
        if body == '':
            return Response({'error': 'request body is empty!'}, status=status.HTTP_400_BAD_REQUEST)
        body =  json.loads(body)
        
        # There, body should be a list
        if type(body) is not list:
            return Response({'Error': "The  body should contain a list!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # After that, test each object in body and save them
        response = []
        for i in range(len(body)):
            serializer = TestSerializer(data=body[i])
            if not serializer.is_valid():
                return Response({"index": i, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
            response.append(serializer.data)
        
        return Response(response, status=status.HTTP_201_CREATED)