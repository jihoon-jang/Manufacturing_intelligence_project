from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
   path('apihome', views.apihome, name="apihome"),
   path('api_view',views.api_view, name="api_view")
]
