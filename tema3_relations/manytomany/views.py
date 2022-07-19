from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):
    art1 = Article(headline = 'Ultimos partidos contra Boca')
    art1.save()

    art2 = Article(headline = 'Ultimos partidos contra Defensa y Justicia')
    art2.save()

    art3 = Article(headline = 'Ultimos partidos contra Independiente')
    art3.save()

    pub1 = Publication(title = "River gana 1-0")
    pub1.save()

    pub2 = Publication(title = "River gana 2-0")
    pub2.save()

    pub3 = Publication(title = "River golea 3-0")
    pub3.save()

    pub4 = Publication(title = "River golea 4-0")
    pub4.save()

    pub5 = Publication(title = "River golea 5-0")
    pub5.save()

    pub6 = Publication(title = "River golea 6-0")
    pub6.save()

    pub7 = Publication(title = "River golea 7-0")
    pub7.save()

    # para crear relaciones:
    art1.publications.add(pub1)
    art1.publications.add(pub4)
    art1.publications.add(pub3)
    art2.publications.add(pub7)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub2)

    # para eliminar relaciones:
    # art1.publications.remove(pub1)

    pub1 = Publication.objects.get(id=1)
    result = pub1.article_set.all()

    return HttpResponse(result)