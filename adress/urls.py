from django.urls import path
from . import views

urlpatterns = [
    path("adress/", views.adress_view, name='adress_view')
]
