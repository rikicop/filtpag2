import django_filters
from .models import Inmueble



class InmuebleFilter(django_filters.FilterSet):

    class Meta:
        model = Inmueble
        fields =['codigo','tipo','ubicacion', 'edo']
