from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def sobre(request):
    return render(request, 'main/sobre.html')

def servicos(request):
    return render(request, 'main/servicos.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def projetos(request):
    return render(request, 'main/projetos.html')

def contato(request):
    return render(request, 'main/contato.html')
