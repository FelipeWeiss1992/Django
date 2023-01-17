from django.db import models
from datetime import datetime

class Alunos(models.Model):
    nome_aluno = models.CharField(max_length=150)
    descricao_profissional = models.TextField()
    descricao_pessoal = models.TextField()
    habilidades = models.CharField(max_length=150)
    comportamento = models.CharField(max_length=150)
    workspace = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)
    data_aluno = models.DateTimeField(default=datetime.now, blank=True)

