from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Dossier)
admin.site.register(ListePresence)
admin.site.register(Internement)
