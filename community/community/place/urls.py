from django.urls import path
from place.views import (
    home_view, 
    search_place_view,
    clear_place_view, 
    search_category_view
)
urlpatterns = [
    path('', home_view, name="home"),
    path('search/', search_place_view, name="search"),
    path('clear-search/', clear_place_view, name="clear_search"),
    path('category/<str:category>', search_category_view, name="category"),
]
