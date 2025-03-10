from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home_view'),
    path("aboutme/", views.aboutme_view, name='aboutme_view'),
    
]
