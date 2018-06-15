from django.shortcuts import render
from .models import Destino, Paquete, Itinerario, Tag
from datetime import date


# Create your views here.
def home(request):
    destino = Destino.objects.filter(estado=True)
    paquete = Paquete.objects.filter(estado=True)[0:6]
    tag = Tag.objects.filter(estado=True)
    return render(request, 'viajes/main.html', {
        'destino': destino,
        'paquete': paquete,
        'tag': tag,
        'itinerario': Itinerario.objects.all()
    })


def destino(request):
    destino = Destino.objects.filter(estado=True)
    return render(request, 'viajes/destinos.html', {
        'destino': destino
    })


def paquetes(request):
    paquete = Paquete.objects.filter(estado=True)
    if request.method == 'POST':
        if request.POST.get('tipo') == "1":
            fecha = request.POST.get('daterange')
            monto = int(request.POST.get('monto'))
            destino_id = int(request.POST.get('selectiondestino'))
            anio = int(fecha[6:11])
            mes = int(fecha[0:2])
            dia = int(fecha[3:5])
            date_ini = date(year=anio, month=mes, day=dia)
            anio1 = int(fecha[19:23])
            mes1 = int(fecha[13:15])
            dia1 = int(fecha[16:18])
            date_fin = date(year=anio1, month=mes1, day=dia1)
            paquete = Paquete.objects.filter(estado=True, destino_id=destino_id, fecha__range=[date_ini, date_fin],
                                             tag__in=[monto])
            print(paquete)
            return render(request, 'viajes/paquetes.html', {
                'paquete': paquete
            })
    else:
        return render(request, 'viajes/paquetes.html', {
            'paquete': paquete
        })


def paquetes_detail(request, id=None):
    paquete = Paquete.objects.get(id=id)
    return render(request, 'viajes/paquete_detail.html', {
        'paquete': paquete, 'paquetesrelacionados': Paquete.objects.filter(estado=True, destino=paquete.destino)
    })
