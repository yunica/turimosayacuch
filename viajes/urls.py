from django.urls import path
from .views import *

app_name = 'viajes'
urlpatterns = [
    path('', home, name='home'),
    path('destino/', destino, name='destino'),
    path('paquetes/', paquetes, name='paquetes'),
    path('paquetes_detail/<int:id>/', paquetes_detail, name='paquetes_detail'),

]
