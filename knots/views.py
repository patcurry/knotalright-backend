from django.views.generic import DetailView
from django.views.generic import ListView
from knots.models import Knot


class KnotDetail(DetailView):
    model = Knot


class KnotList(ListView):
    model = Knot
