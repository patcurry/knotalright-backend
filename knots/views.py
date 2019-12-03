from django.views.generic import DetailView, ListView   
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse

from knots.models import Knot, AlternativeName


class KnotDetail(DetailView):
    model = Knot


class KnotList(ListView):
    model = Knot


class KnotCreate(CreateView):
    model = Knot
    fields = ['name']


class KnotDelete(DeleteView):
    model = Knot
    success_url = '/knots/' 


class AlternativeNameCreate(CreateView):
    model = AlternativeName
    fields = ['name']

    def dispatch(self, request, *args, **kwargs):
        self.knot = Knot.objects.get(slug=self.kwargs.get('slug'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.knot = self.knot
        return super(AlternativeNameCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('knots:knot-detail', kwargs={'slug': self.knot.slug})


#class AlternativeNameDelete(DeleteView):
###    model = AlternativeName
