from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator

from .models import Inmueble, InmuebleImage,Post,Equipo,Contact
from .filters import InmuebleFilter

def home(request):
    items = Post.objects.all()
    equipos = Equipo.objects.all()
    if request.method =="POST":
            name_form = request.POST['namef']
            email_form = request.POST['emailf']
            message_form = request.POST['messagef']
            Contact.objects.create(name=name_form,email=email_form,message=message_form)
            return render(request, 'inmuebles/home.html',{'items':items, 'equipos':equipos})
    else:
            return render(request, 'inmuebles/home.html',{'items':items, 'equipos':equipos})
    return render(request, 'inmuebles/home.html', {'items':items,'equipos':equipos})


def show_all_inmuebles_page(request):
    context = {}

    filtered_inmuebles = InmuebleFilter(request.GET,queryset=Inmueble.objects.all())
    
    context['filtered_inmuebles'] = filtered_inmuebles

    paginated_filtered_inmuebles = Paginator(filtered_inmuebles.qs,6)
    page_number = request.GET.get('page')
    inmueble_page_obj = paginated_filtered_inmuebles.get_page(page_number)

    context['inmueble_page_obj'] = inmueble_page_obj 

    return render(request, 'inmuebles/show_all_inmuebles_page.html',context=context) 
    
   

def detalle_view(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    #Va a filtrar un inmueble en particular
    fotos = InmuebleImage.objects.filter(inmueble=inmueble)
    return render(request, 'inmuebles/detalle.html', {'inmueble':inmueble,'fotos':fotos})

def casa(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/show_casa.html', {'inmuebles':inmuebles})

def oficina(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/show_oficina.html', {'inmuebles':inmuebles})

def comercial(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/show_comercial.html', {'inmuebles':inmuebles})

def lote(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/show_lote.html', {'inmuebles':inmuebles})

def base_two(request):
    
    return render(request, 'inmuebles/base_two.html', {})