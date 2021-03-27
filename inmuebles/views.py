from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator

from .models import Inmueble, InmuebleImage
from .filters import InmuebleFilter

def show_all_inmuebles_page(request):
    context = {}

    filtered_inmuebles = InmuebleFilter(request.GET,queryset=Inmueble.objects.all())
    
    context['filtered_inmuebles'] = filtered_inmuebles

    paginated_filtered_inmuebles = Paginator(filtered_inmuebles.qs,2)
    page_number = request.GET.get('page')
    inmueble_page_obj = paginated_filtered_inmuebles.get_page(page_number)

    context['inmueble_page_obj'] = inmueble_page_obj 



    return render(request, 'inmuebles/show_all_inmuebles_page.html',context=context) 

def detalle_view(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    #Va a filtrar un inmueble en particular
    fotos = InmuebleImage.objects.filter(inmueble=inmueble)
    return render(request, 'inmuebles/detalle.html', {'inmueble':inmueble,'fotos':fotos})