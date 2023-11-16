# Imports
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

# Set URL patterns 
urlpatterns = [
    path("", views.index, name="index")

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)