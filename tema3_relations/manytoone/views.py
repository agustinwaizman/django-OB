from django.shortcuts import render
from .models import Reporter, Article
from datetime import date
from django.http import HttpResponse

def create(request):
    rep = Reporter(first_name = "Agustin", last_name = "Waizman", email = "aguswaizman98@example.com")
    rep.save()

    art1 = Article(headline = "River campeon de la libertadores", pub_date = date(2015, 8, 5), reporter = rep)
    art1.save()
    art2 = Article(headline = "River campeon en el Bernabeu", pub_date = date(2018, 12, 9), reporter = rep)
    art2.save()
    art3 = Article(headline = "River golea en santiago del estero", pub_date = date(2021, 12, 11), reporter = rep)
    art3.save()

    # result = art1.reporter.first_name
    # result = rep.article_set.filter(headline = "River campeon en el Bernabeu")
    result = rep.article_set.count()

    return HttpResponse(result)
