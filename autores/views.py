# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from autores.models import Autor
from autores.serializers import AutorSerializer

# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.object.all()
    serializer_class = AutorSerializer

