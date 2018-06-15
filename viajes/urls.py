from django.urls import path
from .views import *

app_name = 'viajes'
urlpatterns = [
    path('', home, name='home'),
    path('destino/', destino, name='destino'),
    path('paquetes/', paquetes, name='paquetes'),
    path('paquetes/<int:id>/', paquetes_id, name='paquetes_id'),
    path('galeria/', galeria, name='galeria'),
    path('galeria/<int:id>/', galeria_id, name='galeria_id'),
    path('paquetes_detail/<int:id>/', paquetes_detail, name='paquetes_detail'),

]
