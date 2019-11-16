from django.urls import path
from core.views import user, login, cadastro, edit, start_monitoring, close_solenoid

urlpatterns = [
    path('', login, name='login'),
    path('user/<int:user_id>', user, name='user'),
    path('cadastro/<str:code_number>', cadastro, name='cadastro'),
    path('edit/<str:code_number>', edit, name='edit'),
    path('user/<int:user_id>/<int:qtd_water>', start_monitoring, name='monitoring')
    path('user/<int:user_id>/<str:faltante>', close_solenoid, name='close_solenoid')
]
