from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homePage'),
    path('neighborhood/<id>', views.neighborhood, name='neighborhood'),
] 