from django.shortcuts import render
from django.http import HttpResponse

from.models import Alunos

def index(request):
    
    alunos = Alunos.objects.all()

    return render(request, 'index.html', {'alunos': alunos})


def aluno(request):
    return render(request, 'aluno.html')

# Create your views here.
