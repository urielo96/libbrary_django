from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name = 'inicio'),
    path("mi_pagina/", views.mi_pagina, name="mi_pagina"),
    path("libros",views.libros , name="libros"),
    path("libros/crear",views.crear , name="crear"),
    path("(libros/editar",views.editar , name="editar"),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
 
