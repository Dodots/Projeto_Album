from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreateView, PerfilUpdateView
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'usuario/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout"),
    path('cadastro/', UsuarioCreateView.as_view(), name="cadastro"),
    path('atualizar-dados/', PerfilUpdateView.as_view(), name='atualizar-dados')
]