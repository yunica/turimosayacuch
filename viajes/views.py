from django.shortcuts import render
from .models import Destino, Paquete, Itinerario


# Create your views here.
def home(request):
    destino = Destino.objects.filter(estado=True)
    paquete = Paquete.objects.filter(estado=True)[0:6]
    return render(request, 'viajes/main.html', {
        'destino': destino,
        'paquete': paquete,
        'itinerario': Itinerario.objects.all()
    })


def destino(request):
    return render(request, 'viajes/destinos.html', {
        'destino': Destino.objects.filter(estado=True)
    })


def paquetes(request):
    return render(request, 'viajes/paquetes.html', {
        'paquete': Paquete.objects.filter(estado=True)
    })


def paquetes_detail(request, id=None):
    paquete = Paquete.objects.get(id=id)
    return render(request, 'viajes/paquete_detail.html', {
        'paquete': paquete, 'paquetesrelacionados': Paquete.objects.filter(estado=True, destino=paquete.destino)
    })
