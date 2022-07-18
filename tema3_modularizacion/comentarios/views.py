from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment

def test(request):
    return HttpResponse("Funciona Correctamente")

# def create(request):
    # comment = Comment(name="Agustin", score = 5, comment = "este es un comentario")
    # comment.save()
    # comment = Comment.objects.create(name="Micaela")
    # return HttpResponse("Ruta para probar la creacion de modelos")

def delete(request):
    # comment = Comment.objects.get(id=4)
    # comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse("ruta para probar los borrados")