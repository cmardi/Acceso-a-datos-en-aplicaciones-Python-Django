from datetime import datetime
from django.utils.timezone import make_aware
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

 
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255, default='Nombre por defecto')
    ciudad = models.CharField(max_length=255, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre
 
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255, default='Nombre por defecto')
    laboratorio = models.OneToOneField(
        Laboratorio,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Directores Generales"

    def __str__(self):
        return self.nombre
   
class Producto(models.Model):
    nombre = models.CharField(max_length=255, default='Nombre por defecto')
    laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
         
    )
    
    fecha_fabricacion = models.DateTimeField( validators=[MinValueValidator(timezone.make_aware(datetime(2015, 1, 1, 0, 0)))])
    
    p_costo = models.DecimalField(max_digits=13, decimal_places=2)
    p_venta = models.DecimalField(max_digits=13, decimal_places=2)
 
    def __str__(self):
        return self.nombre   
    
class Contador(models.Model):
    visitas = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Visitas: {self.visitas}"