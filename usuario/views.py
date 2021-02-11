from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Perfil

class UsuarioCreateView(CreateView):
    template_name = "usuario/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="membro")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

class PerfilUpdateView(UpdateView):
    template_name = "usuario/form.html"
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone"]
    success_url = reverse_lazy("index")

    def get_object(self):
        self.get_object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.get_object
