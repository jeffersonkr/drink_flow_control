from django.urls import path
from core.views import user, login, cadastro, edit, take_photo

urlpatterns = [
    path('', login, name='login'),
    path('user/<int:user_id>', user, name='user'),
    path('cadastro/<str:code_number>', cadastro, name='cadastro'),
    path('edit/<str:code_number>', edit, name='edit'),
    path('take_photo/<str:code_number>', take_photo, name='take_photo'),
]
