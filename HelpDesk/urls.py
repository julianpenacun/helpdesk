from django.contrib import admin
from django.urls import path
from Solicitud import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.Inicio, name='inicio'),
    path('registro/',views.Registro, name ='registro'),
    path('cierre_sesion/',views.Cierre_Sesion, name='cierre_sesion'),
    path('inicio_sesion/',views.Inicio_Sesion, name='inicio_sesion'),
    path('solicitudes/',views.Solicitud, name='solicitudes'),
    path('solicitudes/todo/',views.Solicitud_Todas, name='solicitudes_todo'),
    path('solicitudes/crear/',views.Crear_Solicitud, name='solicitudes_crear'),
    path('solicitudes/<int:solicitud_id>/', views.Detalle_Solicitud, name="solicitudes_detalle"),
    path('solicitudes/<int:solicitud_id>/completo/', views.Completar_Solicitud, name="solicitudes_completa"),
    path('solicitudes/<int:solicitud_id>/eliminar/', views.Eliminar_Solicitud, name="solicitudes_eliminar"),
    
]