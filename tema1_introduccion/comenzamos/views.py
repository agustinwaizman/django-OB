from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo")

def despedida(request):
    return HttpResponse("Adios, hasta luego")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Sos mayor de edad")
    else:
        return HttpResponse("Sos menor de edad")