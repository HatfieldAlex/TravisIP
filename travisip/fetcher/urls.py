from django.urls import path
from .views import patent_search

urlpatterns = [
    path('patents/', patent_search, name='patent_search'),
]
