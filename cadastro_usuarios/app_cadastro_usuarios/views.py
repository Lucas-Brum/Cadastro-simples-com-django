from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuario
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a pagna de listagem
    return render(request, 'usuarios/usuario.html', usuarios)