from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render

from .models import Note
from .serializers import NoteSerialazer
from django.conf import settings


# Create your views here.


class BlogShow(APIView):

    def get(self, request, format=None):
        notes = Note.objects.all()

        text = []

        for i in notes:
            text.append({
                'id': i.id,
                'title': i.title,
                'message': i.message,
                'username': i.author.username, })
        return Response(text)



class BlogShowGeneric(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerialazer


def blog_version(request):
    x = settings.APP_VERSIONS['blog']

    return render(request, 'blog/index.html', {'x': x})

