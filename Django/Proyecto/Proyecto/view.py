from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader



def index(self):
    
    nom = "Cristiano"
    ap = "Ronaldo"
    
    listaDeDorsales = [69, 80, 94]
    
    nom1 = "Lionel"
    ap1 = "Messi"
    
    listaDeDorsales1 = [72, 90, 96]
    
    nom2 = "Neymar"
    ap2 = "Da Silva"
    
    listaDeDorsales2 = [65, 92, 95]
    
    
    
    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.now(), "Dorsales":listaDeDorsales,
                   "messinombre":nom1, "messiapellido":ap1, "messiDorsales":listaDeDorsales1,
                   "neymarnombre":nom2, "neymarapellido":ap2, "neymarDorsales":listaDeDorsales2
                   }
    
    
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)

