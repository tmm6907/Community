from django.shortcuts import render
from place.models import Place


# Create your views here.
SUPPORTED_REGIONS = "Washington DC, Maryland"


def home_view(request):
    context = {
        'supported_regions': str(SUPPORTED_REGIONS)
    }
    return render(request, 'home.html', context)


def search_place_view(request):
    # displays full list of places by zipcode
    if request.POST.get('zipcode'):
        query = request.POST.get('zipcode')
    else:
        query = request.session.get('zipcode')
    request.session['zipcode'] = query
    places = Place.objects.filter(zip_code=query).order_by('name')
    context = {
        'queryset': places,
        'zipcode': query
    }
    return render(request, 'partials/results_list.html', context)


def search_category_view(request, category):
    # displays subset of list of places by category
    zipcode = request.session.get('zipcode')
    if category == 'health care':
        category=['primary care','pharmacy', 'emergency service', 'dental care']
    
        places = Place.objects.filter(
            zip_code=zipcode,
            category__in=category).order_by('name')
    elif category == 'mail and shipping':
        category=['post office','fedex', 'ups']
    
        places = Place.objects.filter(
            zip_code=zipcode,
            category__in=category).order_by('name')
    else:
        places = Place.objects.filter(
            zip_code=zipcode,
            category=category).order_by('name')
    context = {
        'queryset': places,
        'zipcode': zipcode
    }
    return render(request, 'partials/results_list.html', context)


def clear_place_view(request):
    # responsible for resetting searchbar after submit
    return render(request, 'partials/searchbar.html', {})
