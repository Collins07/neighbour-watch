from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homePage'),
    path('neighborhood/<id>', views.neighborhood, name='neighborhood'),
     path('search/', views.search_business, name='search'),
] 