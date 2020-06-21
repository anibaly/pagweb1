from django.shortcuts import render, HttpResponse

def index(request):
    context = {"pelicula1": "Titanic",
               "pelicula2": "Up",
               "pelicula3": "El señor de los anillos"}
    return render(request, "index.html", context)

def contacto(request):
    return HttpResponse("Mi mail es f@uai.cl")

def t1(request):
    return HttpResponse(":)")
