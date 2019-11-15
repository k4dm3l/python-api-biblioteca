# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Editorial (models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pagina_web = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre