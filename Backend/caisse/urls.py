from django.urls import path, include, re_path
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from compuclinic_api.settings import API_BASE_URL

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Caisse API",
        default_version="v1",
        description="Documentation de l'API du module Caisse",
    ),
    public=True,
    url=API_BASE_URL + "api/caisse-api/",
    urlconf="caisse.urls",
)

router = routers.DefaultRouter()
router.register('bons', views.BonViewSet)
router.register('AGVs', views.AGVViewSet)
router.register('BGSs', views.BGSViewSet)
router.register('BSCs', views.BSCViewSet)
router.register('TIAPSs', views.TIAPSViewSet)
router.register('quittances', views.QuittanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('nombre_quittances_non_consommees/', views.QuittancePatientView.as_view()),
    path('enums/', views.EnumView.as_view()),
    
    # Swagger and Redoc UIS
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]
