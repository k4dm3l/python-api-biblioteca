# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from autores.models import Autor
from editoriales.models import Editorial
from django.utils import timezone

# Create your models here.
class Libro (models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=timezone.now())

    def ___str__(self):
        return self.titulo