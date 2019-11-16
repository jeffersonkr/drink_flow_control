from django.shortcuts import render, redirect
from django.core.files import File
from django.conf import settings
from django.db import IntegrityError
from .forms.user_form import UserForm
from .models.user import User
from .utils.flowmeter import FlowMeter
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

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
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            cellphone = form.cleaned_data.get('cellphone')
            photo = request.FILES.get('photo')
            try:
                User.objects.create(
                    name=name, cellphone=cellphone, code_number=code_number, photo=photo).save()
            except IntegrityError as e:
                context = {
                    'title': 'Cadastro',
                    'error_cel': """<ul class='errorlist'>
                                        <li>O numero informado já possui cadastro</li> 
                                    </ul>""",
                    }
                return  render(request, 'register.html', context)

            return redirect('login')

        else:
            context = {
                'error_nome': form.errors.get("name", ""),
                'error_cel': form.errors.get("cellphone", ""),
                'title': 'Cadastrar'
                }

            return render(request, 'register.html', context)


    return render(request, 'register.html', {'title': 'Cadastrar'})


def edit(request, code_number):
    user = User.objects.get(code_number=code_number)
    context = {
        'title': 'Editar',
        'user_name': user.name,
        'user_cellphone': user.cellphone,
        }
    
    if request.POST:
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            cellphone = form.cleaned_data['cellphone']
            photo = form.cleaned_data.get('photo', request.FILES['photo'])
            print(photo)
            try:
                user.name = name
                user.cellphone = cellphone
                user.photo = photo
                user.save()
            except IntegrityError as e:
                context = {
                    'title': 'Cadastro',
                    'error_cel': """<ul class='errorlist'>
                                        <li>O numero informado já possui cadastro</li> 
                                    </ul>""",
                    }
                return  render(request, 'register.html', context)

        return redirect('user', user.id)

    return render(request, 'register.html', context)


def user(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'title': 'Perfil',
        'user_id': user.id,
        'user_name': user.name,
        'user_cellphone': user.cellphone,
        'user_created': user.created_at,
        'user_updated': user.updated_at,
        'user_code_number': user.code_number,
        'user_photo': user.photo if user.photo else None,
        'user_total_agua_diaria': user.total_water_per_day,
        'user_faltante_agua': user.total_drunk_today,
        'script': "/static/js/choose_timer.js",
    }

    return render(request, 'user.html', context)

def start_monitoring(request, user_id, qtd_water):
    GPIO.OUTPUT(37, 1)
    user = User.objects.get(id=user_id)
    context = {
        'title': 'Perfil',
        'user_id': user.id,
        'user_name': user.name,
        'user_cellphone': user.cellphone,
        'user_created': user.created_at,
        'user_updated': user.updated_at,
        'user_code_number': user.code_number,
        'user_photo': user.photo if user.photo else None,
        'user_total_agua_diaria': user.total_water_per_day,
        'user_faltante_agua': user.total_drunk_today,
        'script': "/static/js/get_monitoring.js",
    }


    return render(request, 'user.html', context)

def logout(request, user_id, faltante):
    GPIO.output(37, 0)
    user = User.objects.get(id=user_id)
    user.total_drunk_today = faltante
    user.save()

    return redirect('login')