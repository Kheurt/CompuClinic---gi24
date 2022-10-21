from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.static import static
from . import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Compuclinic API",
        default_version="v1",
        description="Documentation de l'API de compuclinic",
    ),
    public=True
)


@api_view(['GET'])
def root(request):
    """
    API Entry point
    """

    return Response({
        'CONSULTATION API': request.build_absolute_uri() + 'consultation-api/',
        'CAISSE API': request.build_absolute_uri() + 'caisse-api/',
        'SECRETARIAT API': request.build_absolute_uri() + 'secretariat-api/',
        'GRH API': request.build_absolute_uri() + 'grh-api/',
        'PLATEAU TECHNIQUE API': request.build_absolute_uri() + 'plateau-technique-api/',
        'UTILISATEUR API': request.build_absolute_uri() + 'utilisateur-api/',
    })


urlpatterns = [
    # MISC Routes
    path('api/', root),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger and Redoc UIS
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),

    # API ROUTES
    path('api/consultation-api/', include('consultation.urls')),
    path('api/caisse-api/', include('caisse.urls')),
    path('api/secretariat-api/', include('secretariat.urls')),
    path('api/grh-api/', include('grh.urls')),
    path('api/plateau-technique-api/', include('plateau_technique.urls')),
    path('api/utilisateur-api/', include('utilisateur.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
