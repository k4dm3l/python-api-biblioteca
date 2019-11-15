# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer, CreateEditorialSerializer

# Create your views here.
class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.object.all()
    serializer_class = EditorialSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateEditorialSerializer
        return EditorialSerializer