from django.urls import path
from .views import * 

urlpatterns = [
    path("", index, name = "index" ),  
    path("insertar/", insertar, name = "insertar" ),  
    path("actualizar/<int:id>/", actualizar, name = "actualizar" ),
    path("eliminar/<int:id>/", eliminar, name = "eliminar" ),
]
