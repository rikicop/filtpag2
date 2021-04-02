from django.contrib import admin

from .models import Inmueble, InmuebleImage, Post, Equipo, Contact

admin.site.register(Post)
admin.site.register(Equipo)
admin.site.register(Contact)

class InmuebleImageAdmin(admin.StackedInline):
    model = InmuebleImage
@admin.register(Inmueble)
class PostAdmin(admin.ModelAdmin):
    inlines = [InmuebleImageAdmin]
    class Meta:
       model = Inmueble
@admin.register(InmuebleImage)
class InmuebleImageAdmin(admin.ModelAdmin):
    pass 
