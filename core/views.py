from django.shortcuts import render, redirect
from django.conf import settings
from django.db import IntegrityError
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

        try:
            user = User.objects.get(code_number=code_number)
        except User.DoesNotExist:
            user = None

        if user:
            return redirect('user', User.objects.get(code_number=code_number).id)
        elif not user and len(code_number) == 4:
            return redirect('cadastro', code_number)
        elif len(code_number) > 4 or len(code_number) < 4:
            return render(request, 'login.html', {'error': 'Verifique o código: deve conter 4 dígitos :)'})
        
    return render(request, 'login.html')

def cadastro(request, code_number):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cellphone = form.cleaned_data['cellphone']
            try:
                User.objects.create(
                    name=name, cellphone=cellphone, code_number=code_number).save()
            except IntegrityError as e:
                context = {
                    'error_cel': f"""<ul class='errorlist'>
                                        <li>O numero informado já possui cadastro</li> 
                                    </ul>""",
                    }
                return  render(request, 'register.html', context)

            return redirect('login')

        else:
            context = {
                'error_nome': form.errors.get("name", ""),
                'error_cel': form.errors.get("cellphone", ""),
                'title': 'Cadastro'
                }

            return render(request, 'register.html', context)


    return render(request, 'register.html')

def user(request, user_id):
    user = User.objects.get(id=user_id)

    context = {
        'title': 'Perfil',
        'user_name': user.name,
        'user_cellphone': user.cellphone,
        'user_created': user.created_at,
        'user_updated': user.updated_at,
        'user_code_number': user.code_number,
        'user_photo': user.photo,
    }

    return render(request, 'user.html', context)