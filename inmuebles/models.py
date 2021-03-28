from django.db import models

TODOTIPO='Casa, Apartamento, Lote ...'
CASA = 'Casa'
APARTAMENTO= 'Apartamento'
LOTE = 'Lote'
OFICINA= 'Oficina'

TODOUBI='Ciudad Ojeda, Tamare...'
OJEDA = 'Ciudad Ojeda'
TAMARE ='Tamare'
TIAJUANA ='Tía Juana'

TODOEDO='Nuevo / Usado'
NUEVO = 'Nuevo'
USADO = 'Usado'

TIPO_CHOICES = [(TODOTIPO,TODOTIPO),(CASA,CASA),(APARTAMENTO, APARTAMENTO), (LOTE, LOTE), (OFICINA,OFICINA)]
UBI_CHOICES = [(TODOUBI,TODOUBI), (OJEDA,OJEDA),(TAMARE, TAMARE),(TIAJUANA, TIAJUANA)]
EDO_CHOICES = [(TODOEDO,TODOEDO), (NUEVO,NUEVO),(USADO, USADO),]

class Inmueble(models.Model):
    codigo = models.CharField(max_length=100)
    #codigo = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES ,blank=True)
    ubicacion = models.CharField(max_length=1000, choices=UBI_CHOICES ,blank=True)
    edo = models.CharField(max_length=1000, choices=EDO_CHOICES ,blank=True)
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        template = '{0.codigo} {0.tipo} {0.ubicacion} {0.edo} {0.precio}'
        return template.format(self)

class InmuebleImage(models.Model):
    inmueble = models.ForeignKey(Inmueble, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        template = '{0.inmueble.codigo}'
        #return self.inmueble.codigo
        return template.format(self)
