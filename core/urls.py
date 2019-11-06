from django.urls import path
from core.views import user, login, cadastro

urlpatterns = [
    path('', login, name='login'),
    path('user/', user, name='user'),
    path('cadastro/', cadastro, name='cadastro'),
]
