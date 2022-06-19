from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homePage'),
    path('neighborhood/<id>', views.neighborhood, name='neighborhood'),
    path('search/', views.search_business, name='search'),
    path('<id>/post', views.post, name='post'),
    path('profile/<username>/', views.profile, name='profile'),
    path('enter/<id>', views.enter_neighborhood, name='enter'),
    path('leave/<id>', views.leave_neighborhood, name='leave'),
] 