from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,"paginas/inicio.html")

def mi_pagina(request):
    return render(request,"paginas/mi_pagina.html")

def libros(request):
    return render(request,"libros/index.html")

def crear(request):
    return render(request,"libros/crear.html")

def editar(request):
    return render(request,"libros/editar.html")