from django.urls import path

from knots.views import KnotCreate, KnotDetail, KnotList, KnotDelete
from knots.views import AlternativeNameCreate

app_name = 'knots'

urlpatterns = [
    path('', KnotList.as_view(), name='knot-list'),
    path('create/', KnotCreate.as_view(), name='knot-create'),
    path('<slug:slug>/', KnotDetail.as_view(), name='knot-detail'),
    path('<slug:slug>/delete/', KnotDelete.as_view(), name='knot-delete'),
    path('<slug:slug>/add-name/', AlternativeNameCreate.as_view(), name='add-name'),
]

