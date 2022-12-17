from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

class VenueView(views.APIView):
    
    def get(self, *args, **kwargs):

        return Response("Hit Venue view get method")

