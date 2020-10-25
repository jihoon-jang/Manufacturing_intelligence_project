from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('chart1', views.chart1, name="chart1"),
    path('chart2', views.chart2, name="chart2"),
    path('chart3', views.chart3, name="chart3"),
    path('chart4', views.chart4, name="chart4"),
    path('chart5', views.chart5, name="chart5"),
    path('chart6', views.chart6, name="chart6"),
]
