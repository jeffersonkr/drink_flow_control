from django.urls import path
from core.views import user, login, cadastro, edit, start_monitoring

urlpatterns = [
    path('', login, name='login'),
    path('user/<int:user_id>', user, name='user'),
    path('cadastro/<str:code_number>', cadastro, name='cadastro'),
    path('edit/<str:code_number>', edit, name='edit'),
    path('user/<int:user_id>/OK', start_monitoring, name='monitoring')
]
