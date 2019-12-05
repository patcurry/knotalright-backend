from django.views.generic import DetailView, ListView   
from django.urls import reverse

from knots.models import Knot, AlternativeName


class KnotDetail(DetailView):
    model = Knot


class KnotList(ListView):
    model = Knot
