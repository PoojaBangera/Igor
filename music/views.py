from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Songs, Artists
from .serializers import SongsSerializer, ArtistSerializer
from django.http import HttpResponse


class ListSongsView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class ListArtistsView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer


class CreateArtistsView(generics.CreateAPIView):
    """
    Provides a update method handler.
    """
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer

    def get_query(self):
        return queryset

    # def create(request, *args, **kwargs):
     #   return super(CreateArtistsView, self).create(request, *args, **kwargs)


def index(request):
    html = """<h1> This is the homepage bro, welcome home! </h1>"""
    return HttpResponse(html)

def create_artist(request):
    serializer = ArtistSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Artist added"})
    else:
        data = {
            "error": True,
            "errors": serializer.errors
        }
        return Response(data)
