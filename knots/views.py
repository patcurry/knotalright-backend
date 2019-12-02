from django.views.generic import ListView
from knots.models import Knot


class KnotList(ListView):
    model = Knot
