from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido a la libreria</h1>")

def mi_pagina(request):
    return render(request,"paginas/mi_pagina.html")

def libros(request):
    return render(request,"libros/index.html")