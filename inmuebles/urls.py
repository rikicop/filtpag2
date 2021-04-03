from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('busqueda', views.show_all_inmuebles_page, name="show_all_inmuebles_page"),
    path('<int:id>/', views.detalle_view, name='detalle'),
    path('Casa', views.casa, name="Casa"),
    path('Oficina', views.oficina, name="Oficina"),
    path('Comercial', views.comercial, name="Comercial"),
    path('Lote', views.lote, name="Lote"),
    path('base_two', views.base_two, name="base_two"),
]