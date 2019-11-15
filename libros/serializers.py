from rest_framework import serializers
from libros.models import Libro
from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer

class LibroSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True, read_only=True)
    editorial = EditorialSerializer(read_only=True)
    class Meta:
        model = Libro
        fields = ('titulo', 'autores', 'editorial', 'fecha_publicacion')

class CreateLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('titulo', 'autores', 'editorial', 'fecha_publicacion')