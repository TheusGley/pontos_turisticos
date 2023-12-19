from core.models import Pontos_turisticos
from .serializers import PontosSerializer
from rest_framework.viewsets import ModelViewSet 

class Pontosturistico_Viewsets(ModelViewSet):
    
    queryset = Pontos_turisticos.objects.all()
    serializer_class = PontosSerializer
    


