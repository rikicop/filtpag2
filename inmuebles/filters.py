import django_filters as filters
#import django_filters

from .models import Inmueble


OJEDA = 'Ciudad Ojeda'
TAMARE ='Tamare'
TIAJUANA ='Tía Juana'
UBI_CHOICES = [(OJEDA,OJEDA),(TAMARE, TAMARE),(TIAJUANA, TIAJUANA)]

NUEVO = 'Nuevo'
USADO = 'Usado'
EDO_CHOICES = [ (NUEVO,NUEVO),(USADO, USADO),]

CASA = 'Casa'
APARTAMENTO= 'Apartamento'
LOTE = 'Lote'
OFICINA= 'Oficina'
TIPO_CHOICES = [(CASA,CASA),(APARTAMENTO, APARTAMENTO), (LOTE, LOTE), (OFICINA,OFICINA)]


class InmuebleFilter(filters.FilterSet):
    codigo = filters.CharFilter(label='No. de Código')
    ubicacion = filters.ChoiceFilter(choices=UBI_CHOICES, label='Zona,Ciudad Ojeda,Tamare...')
    edo = filters.ChoiceFilter(choices=EDO_CHOICES, label='Nuevo/Usado/Alquiler...')
    tipo = filters.ChoiceFilter(choices=TIPO_CHOICES, label='Casa,Apartamento...')
    
    class Meta:
        model = Inmueble
        fields =['tipo','ubicacion', 'edo','codigo']
