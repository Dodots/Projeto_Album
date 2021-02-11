from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class UsuarioCreateView(CreateView):
    template_name = "usuario/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="membro")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url

