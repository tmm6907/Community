from django.http import HttpResponse
from miner.miner import search_nearby_place, zipcodes, places


def miner_view(request):
    for zipcode in zipcodes:
        for place in places:
            search_nearby_place(place, zipcode)
    return HttpResponse('<h1> Success!</h1>')
