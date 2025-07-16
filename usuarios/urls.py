
from django.urls import path
from .views import (
    RegistroUsuario,
    LoginUsuario,
    LogoutUsuario,
    editar_perfil,
    enviar_mensaje,
    bandeja_entrada,
    bandeja_salida,
    perfil_publico,  # Asegúrate de que exista en views.py
)
from django.views.generic import TemplateView  

urlpatterns = [
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),
    path('logout_exitoso/', TemplateView.as_view(
        template_name='usuarios/logout_exitoso.html'
    ), name='logout_exitoso'),
    path('perfil/', editar_perfil, name='perfil'),
    path('mensaje/nuevo/', enviar_mensaje, name='enviar_mensaje'),
    path('mensaje/bandeja/', bandeja_entrada, name='bandeja_entrada'),
    path('mensaje/salida/', bandeja_salida, name='bandeja_salida'),
    path('perfil/<int:user_id>/', perfil_publico, name='perfil_publico'),
]