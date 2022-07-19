from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

def create(request):
    place = Place(name="Lugar 1", address = "calle demo 123")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees = 9)
    restaurant.save()

    return HttpResponse(restaurant.place.address)
