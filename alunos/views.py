from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse

from.models import Alunos


def index(request):
    
    alunos = Alunos.objects.all()

    dados = { 'alunos': alunos }

    return render(request, 'index.html', dados)


def aluno(request,aluno_id):

    alunos = get_object_or_404(Alunos, pk = aluno_id)

    aluno_a_exibir = {

        'aluno': alunos

    }

    return render(request, 'aluno.html', aluno_a_exibir)

# Create your views here.

