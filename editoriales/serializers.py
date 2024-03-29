from rest_framework import serializers
from editoriales.models import Editorial

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('nombre', 'direccion', 'pagina_web', 'ciudad')

class CreateEditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('nombre', 'direccion', 'pagina_web', 'ciudad')