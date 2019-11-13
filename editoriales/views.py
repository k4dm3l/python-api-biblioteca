# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer

# Create your views here.
class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.object.all()
    serializer_class = EditorialSerializer