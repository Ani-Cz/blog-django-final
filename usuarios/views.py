from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Perfil, Mensaje
from .forms import RegistroForm, PerfilForm, MensajeForm

User = get_user_model()


class RegistroUsuario(CreateView):
    form_class = RegistroForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')


class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'


class LogoutUsuario(LogoutView):
    next_page = 'login'


@login_required
def ver_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})


@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'usuarios/editar_perfil.html', {
        'form': form,
        'usuario': request.user,
    })


@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user  # ✅ CAMBIADO de "remitente" a "emisor"
            mensaje.save()
            return redirect('bandeja_salida')
    else:
        form = MensajeForm()
    return render(request, 'usuarios/enviar_mensaje.html', {'form': form})


@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')  # ✅ CAMBIADO "destinatario" → "receptor"
    return render(request, 'usuarios/bandeja_entrada.html', {'mensajes': mensajes})


@login_required
def bandeja_salida(request):
    mensajes = Mensaje.objects.filter(emisor=request.user).order_by('-fecha')  # ✅ CAMBIADO "remitente" → "emisor"
    return render(request, 'usuarios/bandeja_salida.html', {'mensajes': mensajes})


def perfil_publico(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    return render(request, 'usuarios/perfil_publico.html', {'usuario': usuario})