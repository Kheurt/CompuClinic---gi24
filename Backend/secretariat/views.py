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

# mycode
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from consultation.models import *

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
import datetime 


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



# my code
        
class GeneratePdf(views.APIView):
        def get(request,self, pk, *args, **kwargs):
            response = HttpResponse(content_type = 'application/pdf')
            d = datetime. date. today().strftime('%Y-%m-%d')
            response['Content-Disposition'] = f'inline; filename="{d}.pdf"'
            # urlsafe_b64decode('generate-pdf', views.generate_pdf, name='generate-pdf')

            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=A4)

            # data to print
            patient_db = Patient.objects.get(id = pk)
            dossier_db = Dossier.objects.get(patient_id = patient_db.id)
            # patient_db = Patient.objects.get(id = dossier_db.patient_id)
            consultation_db = Consultation.objects.get(dossier_id = dossier_db.id)
            #parametre_db = Parametre.objects.get(consultation_id=consultation_db.id)|'null'
            #prescription_db = Prescription.objects.get(consultation_id=consultation_db.id)|'null'
            data = {
                'Info':
                [
                 {'id':patient_db.id},
                 {'name':patient_db.nom},
                #  {'patient':dossier_db.patient_id},
                 {'Prenom':patient_db.prenom},
                 {'NOM':patient_db.nom},
                 {'CNI':patient_db.CNI},
                 {'Dossier_ID':dossier_db.id},
                ], 
                'consulation' : #foreach
                [
                #    {
                #     'date':'consultation_db.date_creation',
                #     'medecin':'consultation_db.medecin',
                #     'parametres':'parametre_db', #foreach
                #     'prescription':'prescription_db', #foreach
                #    }
                ]
            }

            # for consultation in consultation_db :
            #     data['consulation'].append({
            #         'date':consultation.date_creation,
            #         'medecin':consultation.medecin,
            #         'parametres':consultation, #foreach
            #         'prescription':consultation, #foreach
            #        })
            

            # print(patient_db.prenom)
            # print(patient_db.nom)
            # print(patient_db.CNI)
            # print(consultation_db.dossier_id)
            # print(dossier_db.id)

            # {'id':patient_db.id},
            #     {'nom':patient_db.nom},
            #     {'prenom':patient_db.prenom},
            #     {'sex':patient_db.sexe},
            #     {'date_naissance':patient_db.date_naissance},
            #     {'nationalite':patient_db.nationalite},
            #     {'profession':patient_db.profession},
            #     {'antecedent':patient_db.antecedent},
            # http://127.0.0.1:8000/api/secretariat-api/secretariat/44897b52f448403b9edd75de169e9d67/data-you
            # data = {
            #       'id':patient_db.id,
            #       'nom':patient_db.nom,
            #       'prenom':patient_db.prenom
            #   }
            
            # id = f0f4143aa7af41fb814938e97f4a97f7 
            # id = 44897b52f448403b9edd75de169e9d67   
 

            #start writing the PDF here
            p.setFont("Courier-Bold",15,leading=None)
            p.setFillColorRGB(0.29296875, 0.453125, 0.609375)
            p.drawString(260,800,"CompuClinic")
            p.line(0,780,1000,780)
            p.line(0,778,1000,780)
            x1 = 20
            y1 = 750
            
            # Render data
            for k,v in data.items():
                p.setFont("Courier-Bold",20,leading=None)
                p.drawString(x1,y1-20,f"{k}")
                for value in v:
                    for key,val in value.items():
                        p.setFont("Courier-Bold",20,leading=None)
                        p.drawString(x1,y1-20, f"{key} - {val}")
                        y1 = y1-60

            p.setTitle(f'Report on {d}')
            p.showPage()
            p.save()

            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)

            return response

