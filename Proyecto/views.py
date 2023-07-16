from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def saludo(request):
    return HttpResponse("<br><br><h1>Hola,</h1> Este es un test. Si estás aquí por favor escribe el servidor más: /SorteoTique/inicio en el buscador. <br>Si quieres acceder a la lista de ganadores pasados escribe el servidor más: /TiqueExito/landing")

def deSorteo(self, aleatorio):
    data = f"Lo que quiera escribir en negritas: <h1>{aleatorio}</h1>"
    return HttpResponse(data)

def templateTest(self):
    nombre = "Valeria"
    apellido = "Hernandez"

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
    }
    template1= loader.get_template("template.html")
    documento = template1.render(diccionario)
    return HttpResponse(documento)

def about(request):
    return render(request, "about.html")
