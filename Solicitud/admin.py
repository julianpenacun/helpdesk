from django.contrib import admin
from .models import Solicitudes

class SolicitudesAdmin(admin.ModelAdmin):
    readonly_fields=('creado',)


admin.site.register(Solicitudes, SolicitudesAdmin)