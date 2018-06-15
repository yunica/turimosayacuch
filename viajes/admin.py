from django.contrib import admin
from .models import Recurso, Destino, Tag, Paquete, Itinerario, Cupon, Venta

admin.site.register(Recurso)
admin.site.register(Destino)
admin.site.register(Tag)
admin.site.register(Paquete)
admin.site.register(Itinerario)
admin.site.register(Cupon)
admin.site.register(Venta)
