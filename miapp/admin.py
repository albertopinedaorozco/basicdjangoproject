from django.contrib import admin

from .models import Libro, Prestamo, DetallePrestamo, Ejemplar

admin.site.register(Libro)
#admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)
admin.site.register(Ejemplar)

class DetallePrestamoInline(admin.TabularInline):
    model = DetallePrestamo

class PrestamoAdmin(admin.ModelAdmin):
    inlines = [
        DetallePrestamoInline,
    ]

admin.site.register(Prestamo,PrestamoAdmin)


