from django.urls import path

from knots.views import KnotDetail, KnotList

app_name = 'knots'

urlpatterns = [
    path('', KnotList.as_view(), name='knot-list'),
    path('<slug:slug>/', KnotDetail.as_view(), name='knot-detail'),
]

