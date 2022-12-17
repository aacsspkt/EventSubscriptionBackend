

from django.urls import path

from .views import VenueView

urlpatterns = [
    path("", VenueView.as_view()),  
]
