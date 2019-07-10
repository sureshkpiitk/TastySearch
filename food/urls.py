from django.urls import path

from food.views import home, search

urlpatterns = [
    path(r'', home, name='home'),
    path(r'search/', search, name='search'),

]

