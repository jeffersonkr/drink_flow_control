from django.shortcuts import render, redirect
from .forms.user_form import UserForm
from .models.user import User

# Create your views here.


def login(request):
    if request.POST:
        primeiro_digito = request.POST.get('primeiro_digito')
        segundo_digito = request.POST.get('segundo_digito')
        terceiro_digito = request.POST.get('terceiro_digito')
        quarto_digito = request.POST.get('quarto_digito')

        numero = map(str, [primeiro_digito, segundo_digito, terceiro_digito, quarto_digito])
        code_number = "".join(list(numero))
        if code_number == '1234':
            return redirect('user')
        else:
            return redirect('cadastro', code_number)
        
    return render(request, 'login.html')

def cadastro(request, code_number):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cellphone = form.cleaned_data['cellphone']
            User.objects.create(name=name, cellphone=cellphone).save()
            
            return redirect('login')

        else:
            context = {
                'error_nome': form.errors.get("nome", ""),
                'error_cel': form.errors.get("cellphone", "")
                }

            return render(request, 'register.html', context)


    return render(request, 'register.html')

def user(request):
    context = {
    }

    return render(request, 'user.html', context)