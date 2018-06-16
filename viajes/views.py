from django.shortcuts import render
from .models import Destino, Paquete, Itinerario, Tag, Cliente, Venta, Cupon
from datetime import date
from django.db import transaction


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


def galeria(request):
    destino = Destino.objects.filter(estado=True)
    paquete = Itinerario.objects.filter(estado=True)

    return render(request, 'viajes/galeria.html', {
        'destino': destino,
        'paquete': paquete,
    })


def galeria_id(request, id=None):
    destino = Destino.objects.filter(estado=True)
    paquete = Itinerario.objects.filter(estado=True, paquete__destino_id=id)

    return render(request, 'viajes/galeria.html', {
        'destino': destino,
        'paquete': paquete,
    })


def destino(request):
    destino = Destino.objects.filter(estado=True)
    return render(request, 'viajes/destinos.html', {
        'destino': destino
    })


@transaction.atomic
def paquetes(request):
    paquete = Paquete.objects.filter(estado=True)
    destino = Destino.objects.filter(estado=True)

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
                'paquete': paquete,
                'destino': destino,

            })
    else:
        return render(request, 'viajes/paquetes.html', {
            'paquete': paquete,
            'destino': destino,

        })


@transaction.atomic
def paquetes_id(request, id=None):
    paquete = Paquete.objects.filter(estado=True, destino_id=id)
    return render(request, 'viajes/paquetes.html', {
        'paquete': paquete
    })


def paquetes_detail(request, id=None):
    paquete = Paquete.objects.get(id=id)
    return render(request, 'viajes/paquete_detail.html', {
        'paquete': paquete, 'paquetesrelacionados': Paquete.objects.filter(estado=True, destino=paquete.destino)
    })


@transaction.atomic
def reservar(request, id=None):
    if request.method == 'POST':
        paquete = Paquete.objects.get(id=id)
        cliente = Cliente(
            nombre=request.POST.get('nombre'),
            apellidos=request.POST.get('apellido'),
            numdoc=request.POST.get('numdoc'),
            correo=request.POST.get('correo'),
            cel=request.POST.get('cel'),
        )
        cliente.save()
        venta = Venta(nombre=cliente.nombre,
                      apellido=cliente.apellidos,
                      cliente=cliente,
                      paquete=paquete,
                      precio=paquete.precio)
        if request.POST.get('equipaje') == "1":
            venta.idequipaje = True
        venta.pedoequipaje = float(request.POST.get('pesoequipaje'))
        venta.descriobservacionesequipaje = request.POST.get('descripequipaje')
        venta.metodopago = request.POST.get('pago')
        if request.POST.get('iscupon') == "1":
            if Cupon.objects.filter(nombre=request.POST.get('cuponname'), paquete=paquete).exists():
                venta.iscupon = True
                cup = Cupon.objects.get(nombre=request.POST.get('cuponname'), paquete=paquete)
                venta.cupon = cup
                if cup.isporcentaje:
                    venta.precio_final = venta.precio - venta.precio * cup.descuento_decimal
                else:
                    venta.precio_final = venta.precio - cup.descuento_monto
        else:
            venta.precio_final = paquete.precio

        venta.save()
        # paquete.disponibilidad = paquete.disponibilidad - 1
        # paquete.save()
        return render(request, 'viajes/paquetes.html', {
            'paquete': Paquete.objects.filter(estado=True),
            'destino': Destino.objects.filter(estado=True),
        })
    else:
        destino = Destino.objects.filter(estado=True)
        paquete = Paquete.objects.filter(estado=True)[0:6]
        tag = Tag.objects.filter(estado=True)
        return render(request, 'viajes/main.html', {
            'destino': destino,
            'paquete': paquete,
            'tag': tag,
            'itinerario': Itinerario.objects.all()
        })
