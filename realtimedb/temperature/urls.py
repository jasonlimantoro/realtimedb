from django.urls import path
from realtimedb.temperature import views

urlpatterns = [
    path('list', views.TemperatureListView.as_view(), name='temperature_list'),
]
