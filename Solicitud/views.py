from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import FormularioSolicitudes
from .models import Solicitudes

# Función que retorna la visual de la pagina inicial de la aplicación
def Inicio(request):
    return render(request, 'html/index.html')


# Función que retorna la visual con el formulario para registrarse a la aplicación
def Registro(request):

    if (request.method) == 'GET':
        print('enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('solicitudes')
            except IntegrityError:
                return render(request, 'html/registro_usuario.html', {
                    'formulario': UserCreationForm,
                    'error': 'Nombre de usuario ya existe'
                })
        return render(request, 'html/registro_usuario.html', {
            'formulario': UserCreationForm,
            'error': 'La contraseña no coincide'
        })

    return render(request, 'html/registro_usuario.html', {
        'formulario': UserCreationForm
    })


# Decorador que valida que el usuario tenga sesión activa 
@login_required
def Cierre_Sesion(request):
    # Esta función toma el método 'logout' de django para cerrar la sesión activa
    logout(request)
    return redirect('inicio')

def Inicio_Sesion(request):

    if request.method == 'GET':
        return render(request, 'html/inicio_sesion.html', {
            'formulario': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'html/inicio_sesion.html', {
                'formulario': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta',
            })
        else:
            login(request, user)
            return redirect('solicitudes')


@login_required
def Solicitud(request):

    # Control de arreglos por librerias de python "filter, all, etc. explorar mas"
    solicitud = Solicitudes.objects.filter(fecha_finalización__isnull=True)
    return render(request, 'html/solicitud.html', {
        'lista_solicitudes': solicitud,
    })

@login_required
def Solicitud_Todas(request):

    # Control de arreglos por librerias de python "filter, all, etc. explorar mas"
    solicitud = Solicitudes.objects.all
    return render(request, 'html/solicitud.html', {
        'lista_solicitudes': solicitud,
    })

@login_required
def Crear_Solicitud(request):

    if request.method == "GET":

        return render(request, 'html/crear_solicitud.html', {
            'formulario': FormularioSolicitudes
        })

    else:
        try:
            formulario = FormularioSolicitudes(request.POST)
            # Guardará los datos del formulario
            nueva_solicitud = formulario.save(commit=False)
            nueva_solicitud.usuario = request.user
            nueva_solicitud.save()
            print(nueva_solicitud)
            return redirect('solicitudes')

        except ValueError:
            return render(request, 'html/crear_solicitud.html', {
                'formulario': FormularioSolicitudes,
                'error': 'Por favor validar los campos',
            })

@login_required
def Detalle_Solicitud(request, solicitud_id: int):

    if request.method == 'GET':

        solicitud = get_object_or_404(Solicitudes, pk=solicitud_id, usuario = request.user)
        formulario = FormularioSolicitudes(instance=solicitud)
        return render(request, 'html/detalle_solicitud.html',
                    {
                        'solicitud': solicitud,
                        'formulario': formulario,
                    })
    else:
        try:
            solicitud = get_object_or_404(Solicitudes, pk=solicitud_id, usuario = request.user)
            formulario = FormularioSolicitudes(request.POST, instance=solicitud)
            formulario.save()
            return redirect('solicitudes')
        except ValueError:
            return render(request, 'html/detalle_solicitud.html',
                    {
                        'solicitud': solicitud,
                        'formulario': formulario,
                        'error': "Error al actualizar la solicitud"
                    })

@login_required        
def Completar_Solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitudes, pk=solicitud_id, usuario=request.user)

    if request.method == 'POST':
        solicitud.fecha_finalización = timezone.now()
        solicitud.save()
        return redirect('solicitudes')

@login_required    
def Eliminar_Solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitudes, pk=solicitud_id, usuario=request.user)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('solicitudes')

