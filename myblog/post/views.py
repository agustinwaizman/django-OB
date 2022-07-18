from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Entry

def update(request):
    author = Author.objects.get(id=1)
    author.name = "agustin"
    author.email = "aguswaizman98@example.com"
    author.save()
    return HttpResponse("Actualizado correctamente")

def queries(request):
    # obtener todos los elementos
    authors = Author.objects.all()

    # obtener datos filtrando por condicion
    # filtered = Author.objects.filter(email='tracy06@example.org')

    # obtener un unico objeto (filtrado)
    author = Author.objects.get(id=32)

    # obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # obtener 5 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    # obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')

    # obtener elementos cuyo id sea menor o igual a 15
    # filtered = Author.objects.filter(id__lte = 15)

    # obtener todos los autores que contienen en su nombre la palabra yes
    filtered = Author.objects.filter(name__contains = "the")

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits' : limits, 'offsets': offsets, 'orders': orders})