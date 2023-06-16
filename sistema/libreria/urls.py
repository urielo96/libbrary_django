from django.urls import path
from . import views


urlpatterns = [
    path('',views.inicio,name = 'inicio'),
    path("mi_pagina/", views.mi_pagina, name="mi_pagina"),
    path("libros",views.libros , name="libros"),
    path("libros/crear",views.crear , name="crear"),
    path("(libros/editar",views.editar , name="editar"),
    


   
    
    ]
