from django.urls import path

from knots.views import KnotCreate, KnotDetail, KnotList


urlpatterns = [
    path('', KnotList.as_view(), name='knot-list'),
    path('create/', KnotCreate.as_view(), name='knot-create'),
    path('<slug:slug>/', KnotDetail.as_view(), name='knot-detail'),
]

