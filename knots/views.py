from django.views.generic import DetailView, ListView   
from django.views.generic.edit import CreateView

from knots.models import Knot


class KnotDetail(DetailView):
    model = Knot


class KnotList(ListView):
    model = Knot


class KnotCreate(CreateView):
    model = Knot
    fields = ['name']
