from django.shortcuts import render
from django.http import HttpResponse

from.models import Alunos

def index(request):
    
    alunos = Alunos.objects.all()

    dados = { 'alunos': alunos }

    return render(request, 'index.html', dados)


def aluno(request):
    return render(request, 'aluno.html')

# Create your views here.
