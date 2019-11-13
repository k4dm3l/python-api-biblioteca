# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Libro (models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.CharField(max_length=100)

    def ___str__(self):
        return self.titulo