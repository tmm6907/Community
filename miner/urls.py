from django.urls import path
from miner.views import miner_view

urlpatterns = [
    path('miner/', miner_view, name="miner"),
]
