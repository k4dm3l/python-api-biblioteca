from rest_framework import serializers
from autores.models import Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('nombres', 'apellidos', 'correo', 'telefono')