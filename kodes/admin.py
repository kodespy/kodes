from django.contrib import admin

from kodes.models import Usuario
from .models import Compras, ComprasDetalle

admin.site.register(Usuario)
admin.site.register(Compras)
admin.site.register(ComprasDetalle)

