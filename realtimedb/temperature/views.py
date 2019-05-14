from django.views.generic.list import ListView
from .models import Temperature


class TemperatureListView(ListView):
    template_name = 'temperature/temperature_list.html'
    model = Temperature
