# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from libros.models import Libro
from libros.serializers import LibroSerializer, CreateLibroSerializer

from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLibroSerializer
        return LibroSerializer
    
    @action(detail=True, method=['GET'])
    def autores(self, request, pk=None):
        libro = self.get_object()
        autores = libro.autores.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    @action(detail=True, method=['GET'])
    def editoriall(self, request, pk=None):
        libro = self.get_object()
        editorial = libro.editorial
        serilizer = EditorialSerializer(editorial)
        return Response(status=status.HTTP_200_OK, data=serilizer.data)