from django.urls import path, include
from .views import register

urlpatterns = [
path('cadastro/', register, name='register')
#path('login/', , name='login')
]