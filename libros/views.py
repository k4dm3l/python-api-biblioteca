# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from libros.models import Libro
from libros.serializers import LibroSerializer

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.object.all()
    serializer_class = LibroSerializer
