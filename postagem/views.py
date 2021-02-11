from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Postagem
from django.urls import reverse_lazy

class PostagemCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Postagem
    fields = ['titulo', 'descricao', 'foto_postagem']
    template_name = 'postagem/form-upload.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        #Antes do super não foi criado o objeto e não salvou nada.
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
       
        #Depois do super o objeto é criado
        return url

class PostagemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Postagem
    fields = ['titulo', 'descricao', 'foto_postagem']
    template_name = 'postagem/form-upload.html'
    success_url = reverse_lazy('dashboard')

class PostagemDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Postagem
    template_name = 'postagem/form-excluir.html'
    success_url = reverse_lazy('dashboard')

class PostagensListView(ListView):
    model = Postagem
    template_name = 'index.html'

class PostagemDetailView(DetailView):
    model = Postagem
    template_name = 'postagem/postagem.html'

class DashboardListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Postagem
    template_name = 'usuario/dashboard.html'

    def get_queryset(self):
        self.object_list = Postagem.objects.filter(usuario=self.request.user)
        return self.object_list

