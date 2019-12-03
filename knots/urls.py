from django.urls import path

from knots.views import KnotDetail
from knots.views import KnotList


urlpatterns = [
    path('', KnotList.as_view(), name='knot_list'),
    path('<slug:slug>/', KnotDetail.as_view(), name='knot_detail'),
]

