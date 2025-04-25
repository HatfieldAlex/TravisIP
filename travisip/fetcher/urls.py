from django.urls import path
from . import views

urlpatterns = [
    path('patents/', views.patent_search, name='patent_search'),
]
