# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Autor (models.Model):
     nombres = models.CharField(max_length=100)
     apellidos = models.CharField(max_length=100)
     correo = models.CharField(max_length=100)
     telefono = models.CharField(max_length=100)

     def ___str__(self):
        return self.nombre
