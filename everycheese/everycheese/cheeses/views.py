from django.views.generic import ListView, DetailView
from .models import Cheese
from django.views.generic import CreateView


class CheeseListView(ListView):
    model = Cheese


class CheeseDetailView(DetailView):
    model = Cheese


class CheeseCreateView(CreateView):
    fields = [
        'name',
        'description',
        'firmness',
        'country_of_origin',
    ]
    model = Cheese
