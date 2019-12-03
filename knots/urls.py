from django.urls import path

from knots.views import KnotCreate, KnotDetail, KnotList, AlternativeNameCreate


urlpatterns = [
    path('', KnotList.as_view(), name='knot-list'),
    path('create/', KnotCreate.as_view(), name='knot-create'),
    path('<slug:slug>/', KnotDetail.as_view(), name='knot-detail'),
    path('<slug:slug>/add-name', AlternativeNameCreate.as_view(), name='add-name'),
]

