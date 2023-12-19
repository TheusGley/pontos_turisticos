from rest_framework.serializers import ModelSerializer
from core.models import Pontos_turisticos

class PontosSerializer(ModelSerializer):
    class Meta:
        model = Pontos_turisticos
        fields= ('id', 'nome', 'descricao')









