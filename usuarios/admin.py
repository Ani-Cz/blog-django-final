from django.contrib import admin

from .models import Perfil

admin.site.register(Perfil)

from .models import Mensaje

admin.site.register(Mensaje)