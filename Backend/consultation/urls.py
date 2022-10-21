from django.urls import path, include, re_path
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from compuclinic_api.settings import API_BASE_URL

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Consultation API",
        default_version="v1",
        description="Documentation de l'API du module Consultation",
    ),
    public=True,
    url=API_BASE_URL + "api/consultation-api/",
    urlconf="consultation.urls",
)

router = routers.DefaultRouter()
router.register('consultations', views.ConsultationViewSet)
router.register('parametres', views.ParametreViewSet)
router.register('symptomes', views.SymptomeViewSet)
router.register('differentiels', views.DifferentielViewSet)
router.register('recommandations', views.RecommandationViewSet)
router.register('prescriptions-examen', views.PrescriptionExamenViewSet)
router.register('prescriptions-medicament', views.PrescriptionMedicamenteuseViewSet)
router.register('examens', views.ExamenViewSet)
router.register('BulletinExamen', views.BulletinExamenViewSet)
router.register('tests', views.TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('enums/', views.EnumView.as_view()),
    path('parametres-bulk/', views.ParametreBulkCreateView.as_view()),
    path('symptomes-bulk/', views.SymptomeBulkCreateView.as_view()),
    path('differentiels-bulk/', views.DifferentielBulkCreateView.as_view()),
    path('recommadations-bulk/', views.RecommandationBulkCreateView.as_view()),
    path('prescription-examen-bulk/', views.PrescriptionExamenBulkCreateView.as_view()),
    path('prescription-medicament-bulk/', views.PrescriptionMedicamenteuseBulkCreateView.as_view()),
    path('examen-bulk/', views.ExamenBulkCreateView.as_view()),
    path('test-bulk/', views.TestBulkCreateView.as_view()),
    path('consultations/<pk>/fermer/', views.FermerConsultationView.as_view()),
    
    # Swagger and Redoc UIS
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]
