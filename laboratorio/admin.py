from django.contrib import admin
from .models import *

class LaboratorioAdmin(admin.ModelAdmin):
    fields = ['nombre', 'ciudad', 'pais']
    list_display = ['id', 'nombre']
    ordering = ['-id']
    
class DirectorGeneralAdmin(admin.ModelAdmin):
    fields = ['nombre', 'laboratorio']
    list_display = ['id', 'nombre', 'laboratorio']
    ordering = ['-id']
    
class ProductoAdmin(admin.ModelAdmin):
    fields = ['nombre', 'laboratorio', 'fecha_fabricacion', 'p_costo', 'p_venta']
    list_display = ['id', 'nombre', 'laboratorio', 'fecha_fabricacion', 'p_costo', 'p_venta']
    ordering = ['-id']
    list_filter = ['nombre', 'laboratorio']

    
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contador)



