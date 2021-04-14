import django_filters as filters
#import django_filters

from .models import Inmueble


OJEDA = 'Ciudad Ojeda'
TAMARE ='Tamare'
TIAJUANA ='Tía Juana'
LAGUNILLAS ='Lagunillas'
MARACAIBO ='Maracaibo'
CABIMAS = 'Cabimas'
UBI_CHOICES = [(OJEDA,OJEDA),(TAMARE, TAMARE),(TIAJUANA, TIAJUANA),(LAGUNILLAS, LAGUNILLAS),(MARACAIBO,MARACAIBO),(CABIMAS,CABIMAS)]
NUEVO = 'Nuevo'
USADO = 'Usado'
EDO_CHOICES = [ (NUEVO,NUEVO),(USADO, USADO),]

VENTA = 'Venta'
ALQUILER = 'Alquiler'
PROPOSITO_CHOICES = [ (VENTA,VENTA),(ALQUILER, ALQUILER),]


CASA = 'Casa'
APARTAMENTO= 'Apartamento'
LOTE = 'Lote'
OFICINA= 'Oficina'
COMERCIAL='Comercial'
TOWNHOUSE='Townhouse'
TIPO_CHOICES = [(CASA,CASA),(APARTAMENTO, APARTAMENTO), (LOTE, LOTE), (OFICINA,OFICINA),(COMERCIAL,COMERCIAL),(TOWNHOUSE, TOWNHOUSE)]


class InmuebleFilter(filters.FilterSet):
    codigo = filters.CharFilter(label='No. de Código')
    ubicacion = filters.ChoiceFilter(choices=UBI_CHOICES, label='Zona,Ciudad Ojeda,Tamare...')
    #edo = filters.ChoiceFilter(choices=EDO_CHOICES, label='Venta/Alquiler/...')
    proposito = filters.ChoiceFilter(choices=PROPOSITO_CHOICES, label='Venta o Alquiler')
    tipo = filters.ChoiceFilter(choices=TIPO_CHOICES, label='Casa,Apartamento...')
    
    class Meta:
        model = Inmueble
        fields =['tipo','ubicacion', 'proposito','codigo']
