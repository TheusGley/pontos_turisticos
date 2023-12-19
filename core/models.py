from django.db import models
from atracoes.models import Atracao 
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Endereco



class Pontos_turisticos( models.Model):
    
    nome = models.CharField( max_length=50)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField("atracoes.Atracao",)
    comentario = models.ManyToManyField("comentarios.Comentario",)
    avaliacao = models.ManyToManyField("avaliacoes.Avaliacao",)
    endereco = models.ManyToManyField("localizacao.Endereco",)
    
    
    
    def __str__(self) :
        return self.nome
    
    