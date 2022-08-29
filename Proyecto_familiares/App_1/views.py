from django.shortcuts import render
from django.http import HttpResponse
from App_1.models import Familiar
from django.template import loader


# Create your views here.

def familiar(self):
    familiar_1 = Familiar(nombre= "Martín", edad = 21, DNI = 43030795, fecha_de_nacimiento = "2000-11-10", vinculo_familiar = "Yo" )
    familiar_2 = Familiar(nombre= "Gustavo", edad = 65, DNI = 12411281, fecha_de_nacimiento = "1957-11-10", vinculo_familiar = "Padre" )
    familiar_3 = Familiar(nombre= "Aquiles", edad = 1, DNI = 0, fecha_de_nacimiento = "2020-09-06", vinculo_familiar = "Perro" )
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    nueva_linea: str = "\n"
    texto: str =f"Se han creado los familiares"
    return HttpResponse(texto)

def inicio(request):
    diccionario: dict = {"Yo": ["Martín", 21, 43030795, "2000-11-10", "Yo"], "Padre": ["Gustavo", 65, 12411281, "1957-11-10", "Padre"], "Perro": ["Aquiles", 1, 0, "2020-09-06", "Perro"]}
    inicio = loader.get_template("inicio.html")
    documento = inicio.render(diccionario)
    return HttpResponse(documento)