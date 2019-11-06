from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    if request.POST:
        primeiro_digito = request.POST.get('primeiro_digito')
        segundo_digito = request.POST.get('segundo_digito')
        terceiro_digito = request.POST.get('terceiro_digito')
        quarto_digito = request.POST.get('quarto_digito')

        numero = map(str, [primeiro_digito, segundo_digito, terceiro_digito, quarto_digito])
        codigo = "".join(list(numero))
        if codigo == '1234':
            return redirect('user')
        else:
            return redirect('cadastro')
        
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'register.html')

def user(request):
    context = {
    }

    return render(request, 'user.html', context)