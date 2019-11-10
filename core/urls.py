from django.urls import path
from core.views import user, login, cadastro, edit

urlpatterns = [
    path('', login, name='login'),
    path('user/<int:user_id>', user, name='user'),
    path('cadastro/<str:code_number>', cadastro, name='cadastro'),
    path('edit/<str:code_number>', edit, name='edit'),
]
