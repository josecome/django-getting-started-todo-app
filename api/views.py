from rest_framework import viewsets
from django.http import HttpResponse as Response
from rest_framework import status

from .serializers import (
    TodoItemSerializer,
    )
from main.models import (
    TodoItem,
    )
from datetime import date, datetime


class HomeModelViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    def create(self, request, *args, **kwargs):

        data = {'name': request.POST.get("name"), 'completed': 0, 'is_deleted': 0}

        serializer = self.serializer_class(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response('Saved!', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
