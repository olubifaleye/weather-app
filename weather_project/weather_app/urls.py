# Imports
from django.urls import path
from . import views

# Set URL patterns 
urlpatterns = [
    path("", views.index, name="index")

]