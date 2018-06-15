from django.db import models
from django.contrib.auth.models import User


class Recurso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    capacidad = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Destino(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='destino')
    ubicacion = models.CharField(max_length=255,null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Tag(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Paquete(models.Model):
    nombre = models.CharField(max_length=255)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    frase = models.TextField(null=True, blank=True)
    duracion = models.PositiveSmallIntegerField()
    fecha = models.DateField()
    portada = models.ImageField(upload_to='paquete')
    imagen = models.ImageField(upload_to='paquete')
    disponibilidad = models.PositiveSmallIntegerField()
    tag = models.ManyToManyField(Tag)
    precio = models.DecimalField(max_digits=14, decimal_places=4)
    precio_oferta = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    isoferta = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Itinerario(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='itinerario', blank=True, null=True)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Cupon(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descuento_decimal = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    descuento_monto = models.PositiveSmallIntegerField(blank=True, null=True)
    isporcentaje = models.BooleanField(default=True)
    isvalid = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    descriobservaciones = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=14, decimal_places=4)
    precio_final = models.DecimalField(max_digits=14, decimal_places=4)
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE, blank=True)
    iscupon = models.BooleanField(default=False)
    ispago = models.BooleanField(default=False)
    fecpago = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecregistro = models.DateTimeField(auto_now_add=True)
    fecactualizacion = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
