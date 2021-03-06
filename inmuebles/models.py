from django.db import models
import time
import os
from uuid import uuid4

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

CASA = 'Casa'
APARTAMENTO= 'Apartamento'
TOWNHOUSE ='Townhouse'
LOTE = 'Lote'
OFICINA= 'Oficina'
COMERCIAL= 'Comercial'

OJEDA = 'Ciudad Ojeda'
TAMARE ='Tamare'
TIAJUANA ='Tía Juana'
LAGUNILLAS ='Lagunillas'
MARACAIBO ='Maracaibo'
CABIMAS = 'Cabimas'

VENTA = 'Venta'
ALQUILER = 'Alquiler'

NUEVO = 'Nuevo'
USADO = 'Usado'




# TIPO_CHOICES va a llevar mas que POST_CHOICES
TIPO_CHOICES = [(CASA,CASA),(APARTAMENTO, APARTAMENTO), (TOWNHOUSE,TOWNHOUSE),(LOTE, LOTE), (OFICINA,OFICINA),(COMERCIAL,COMERCIAL)]

UBI_CHOICES = [(OJEDA,OJEDA),(TAMARE, TAMARE),(TIAJUANA, TIAJUANA),(LAGUNILLAS, LAGUNILLAS),(MARACAIBO,MARACAIBO),(CABIMAS,CABIMAS)]

PROPOSITO_CHOICES = [ (VENTA,VENTA),(ALQUILER, ALQUILER),]

EDO_CHOICES = [ (NUEVO,NUEVO),(USADO, USADO),]

POST_CHOICES =[(CASA,CASA),(APARTAMENTO,APARTAMENTO),(LOTE, LOTE),(OFICINA,OFICINA),(COMERCIAL,COMERCIAL)]

class Inmueble(models.Model):
    codigo = models.CharField(max_length=100)
    #codigo = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES ,blank=True, default='Error')
    ubicacion = models.CharField(max_length=1000, choices=UBI_CHOICES ,blank=True)
    proposito = models.CharField(max_length=1000, choices=PROPOSITO_CHOICES ,blank=True)
    edo = models.CharField(max_length=1000, choices=EDO_CHOICES ,blank=True)
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField()
    image = models.FileField(upload_to=('here/{}'.format(time.strftime("%Y/%m/%d"))),blank=True)
    posting = models.CharField(max_length=1000, choices=POST_CHOICES ,blank=True)
    """ enlace = models.URLField(choices=POST_CHOICES, max_length=128, blank=True) """
    

    def __str__(self):
        template = '{0.codigo} {0.tipo} {0.ubicacion} {0.proposito} {0.edo} {0.precio}'
        return template.format(self)

class InmuebleImage(models.Model):
    inmueble = models.ForeignKey(Inmueble, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'here/images/{}'.format(time.strftime("%Y/%m/%d")))

    def __str__(self):
        template = '{0.inmueble.codigo}'
        #return self.inmueble.codigo
        return template.format(self)


class Contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=500,blank=False)
    def __str__(self):
        template = '{0.name} {0.email} {0.message}'
        return template.format(self)   

class Post(models.Model):
    name = models.CharField(max_length=300)
    img = models.FileField(blank=True)
    details = models.CharField(max_length=1000, choices=POST_CHOICES ,blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

class Equipo(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    message = models.TextField(max_length=500,blank=True)
    img = models.FileField(blank=True)
    

    def __str__(self):
        template = '{0.title} {0.subtitle}'
        return template.format(self)
