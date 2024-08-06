from django.shortcuts import render
from  .models import Usuario # se models está na mesma pasta que views, tem que usar .models

# Create your views here.

"""
O nome da função é home e porque foi o nome especificado na url;
request --> permite acessar os dados da pagina
render --> renderiza uma pagina
"""
def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    novo_usuario = Usuario()
    # extraí as informações da tela e coloca dentro de um novo usuário
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    # salva os dados do novo usuário no banco de dados
    novo_usuario.save()
    
    # Exibir os usuários já cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all() # retorna todos os usuários que estão np banco de dados
    }
    return render(request, 'usuarios/usuarios.html',usuarios)
    
    
    
    