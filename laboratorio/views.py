from django.shortcuts import render, redirect
from .models import *

def index(request):
    laboratorios = Laboratorio.objects.all().order_by("nombre")
    
    contador, created = Contador.objects.get_or_create(id=1)
    contador.visitas += 1
    contador.save()
    
    context = { "laboratorios": laboratorios,
                "visitas": contador.visitas
              }
    
    return render(request, "index.html", context)

def insertar(request):
    if request.method == "POST":
        # se rescatan los valores del formulario
        nombre = request.POST.get("nombre")
        ciudad = request.POST.get("ciudad")
        pais = request.POST.get("pais")
        
        nuevo_lab = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        
        nuevo_lab.save()
        return redirect("/")
    else:
        return render(request, "insertar.html", {})
    
def actualizar(request, id):
    # Se rescatan los datos del laboratorio
    laboratorio = Laboratorio.objects.get(id=id)
    
    if request.method == "POST":
        # se rescatan los valores del formulario
        nombre = request.POST.get("nombre")
        ciudad = request.POST.get("ciudad")
        pais = request.POST.get("pais")
        
        # se modifican los atributos utilizando
        # los datos enviados por el usuario
        laboratorio.nombre = nombre
        laboratorio.ciudad = ciudad
        laboratorio.pais = pais
        
        # guardo la instancia
        laboratorio.save()
        # redirijo al index
        return redirect("/")
    else:
        context = { "laboratorio": laboratorio }
        return render(request, "actualizar.html", context)
    
def eliminar(request, id):
    
    
    lab_elim = Laboratorio.objects.get(id=id)

    if request.method == "POST":
        lab_elim.delete()
        return redirect("/")
    else:
        context = { "lab_elim": lab_elim }
        return render(request, "eliminar.html", context)
    
    
  