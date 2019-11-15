# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets

from autores.models import Autor
from autores.serializers import AutorSerializer, CreateAutorSerializer

# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAutorSerializer
        return AutorSerializer

