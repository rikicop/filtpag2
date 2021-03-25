from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_all_inmuebles_page, name="show_all_inmuebles_page"),
]