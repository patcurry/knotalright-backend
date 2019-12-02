from django.urls import path
from knots.views import KnotList


urlpatterns = [
    path('', KnotList.as_view(), name='home_list'),
]

